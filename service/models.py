import datetime

from django.db import models

from authenticate.models import Employee, User


class Spare(models.Model):
    SpareCategory = (
        ("body", "BODY"),
        ("engine", "ENGINE"),
        ("transmission", "TRANSMISSION"),
        ("chassis", "CHASSIS"),
        ("electronic", "ELECTRONIC"),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=False)
    category = models.CharField(choices=SpareCategory)
    image = models.ImageField(upload_to='spares/', blank=True, null=True)


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    Status = (
        ("in process", "IN PROCESS"),
        ("ready", "READY"),
    )
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_time = models.DateTimeField(default=datetime.datetime.now())
    status = models.CharField(choices=Status)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь', related_name='orders', default=None)
    repair_request = models.OneToOneField('RepairRequest', related_name='order', on_delete=models.CASCADE, null=True,
                                          blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', related_name='services', on_delete=models.CASCADE)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    spare = models.ForeignKey('Spare', related_name='order_item', on_delete=models.DO_NOTHING, null=True, blank=True)


class RepairRequest(models.Model):
    problem = models.TextField()
    execution_deadline = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    employees = models.ManyToManyField(Employee, related_name='repair_requests', blank=True)
    services = models.ManyToManyField(Service, related_name='repair_requests', blank=True)
