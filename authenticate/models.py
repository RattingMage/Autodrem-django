from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    license_plate = models.CharField(max_length=10, unique=True, verbose_name="Государственный номер")
    brand = models.CharField(max_length=100, verbose_name="Марка")
    vin = models.CharField(max_length=17, unique=True, verbose_name="ВИН")


class User(AbstractUser):
    car = models.ForeignKey('Car', related_name='cars', on_delete=models.CASCADE, blank=True, null=True)


class Employee(User):
    Position = (
        ("not determined", "NOT DETERMINED"),
        ("support ", "SUPPORT"),
        ("mechanic", "MECHANIC"),
    )
    employee_id = models.CharField(max_length=10, unique=True)
    inn = models.CharField(max_length=12)
    position = models.CharField(choices=Position, default=Position[0])
