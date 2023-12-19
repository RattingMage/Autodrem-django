from rest_framework import serializers
from .models import Spare, Service, Order, OrderItem, RepairRequest


class SpareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spare
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    spare = SpareSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = '__all__'


class RepairRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairRequest
        fields = '__all__'
