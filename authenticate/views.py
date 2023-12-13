from django.contrib.auth import get_user_model, login, logout
import logging
from rest_framework import generics, permissions, status
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection, transaction
from authenticate.forms import SQLImportForm
from authenticate.models import Car
from authenticate.serializers import RegistrationSerializer, LoginSerializer, UserSerializer, UpdatePasswordSerializer, \
    CarSerializer
from rest_framework.response import Response

USER_MODEL = get_user_model()

logger = logging.getLogger("main")


class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        logger.debug("registration request")
        return super().post(request, *args, **kwargs)


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            login(request=request, user=user)
        logger.debug("authorization request")
        return Response(serializer.data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = USER_MODEL.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    # @method_decorator(ensure_csrf_cookie)
    # def dispatch(self, *args, **kwargs) -> Response:
    #     return super().dispatch(*args, **kwargs)

    def get_object(self):
        user = self.request.user
        user_with_cars = USER_MODEL.objects.prefetch_related('car').get(pk=user.pk)
        logger.debug("login request")
        return user_with_cars

    def delete(self, request, *args, **kwargs):
        logout(request)
        logger.debug("logout request")
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        car_instance = serializer.save()

        self.request.user.car = car_instance
        self.request.user.save()

        logger.debug("add car request")


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


def import_sql_data(request):
    if request.method == 'POST':
        form = SQLImportForm(request.POST, request.FILES)
        if form.is_valid():
            file_content = request.FILES['file'].read().decode('utf-8')
            try:
                with connection.cursor() as cursor:
                    cursor.execute(file_content)
            except Exception as e:
                messages.error(request, f"Ошибка выполнения SQL-запросов: {e}")
            else:
                messages.success(request, "Данные успешно импортированы.")
                return redirect('admin:authenticate_car_changelist')
    else:
        form = SQLImportForm()

    return render(request, 'admin/import_sql_data.html', {'form': form})