from django.contrib.auth import get_user_model, login, logout
import logging
from rest_framework import generics, permissions, status

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
