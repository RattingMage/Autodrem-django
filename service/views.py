from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

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


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemCreateView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


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
