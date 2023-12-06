from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Spare, Service, Order, OrderItem, RepairRequest
from .serializers import SpareSerializer, ServiceSerializer, OrderSerializer, OrderItemSerializer, \
    RepairRequestSerializer


class ListViewPagination(PageNumberPagination):
    page_size = 10  # Количество объектов на одной странице
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SpareListCreateView(generics.ListCreateAPIView):
    queryset = Spare.objects.all()
    serializer_class = SpareSerializer
    pagination_class = ListViewPagination


class SpareDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spare.objects.all()
    serializer_class = SpareSerializer


class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = ListViewPagination


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = ListViewPagination

    def create(self, request, *args, **kwargs):
        # Добавьте вашу логику для создания заказа, например, получение данных из запроса
        # ...
        # Создание заказа
        order_serializer = self.get_serializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order = order_serializer.save()

        # Возвращаем созданный заказ с кодом 201 (Created)
        headers = self.get_success_headers(order_serializer.data)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemCreateView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        # Получаем заказ, к которому нужно добавить элемент
        order_id = self.request.data.get('order')
        order = Order.objects.get(pk=order_id)

        # Вы можете добавить свою логику для проверки, что заказ в статусе, позволяющем добавление элементов

        # Сохраняем элемент в заказ
        serializer.save(order=order)


# Дополнительное представление для обновления и удаления OrderItem
class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class RepairRequestListCreateView(generics.ListCreateAPIView):
    queryset = RepairRequest.objects.all()
    serializer_class = RepairRequestSerializer


class RepairRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RepairRequest.objects.all()
    serializer_class = RepairRequestSerializer
