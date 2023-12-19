from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Employee(User):
    Position = (
        ("not determined", "NOT DETERMINED"),
        ("support ", "SUPPORT"),
        ("mechanic", "MECHANIC"),
    )
    employee_id = models.CharField(max_length=10, unique=True)
    inn = models.CharField(max_length=12)
    position = models.CharField(choices=Position, default=Position[0])

    class Meta:
        verbose_name = 'Механики'
        verbose_name_plural = 'Механики'


class Car(models.Model):
    license_plate = models.CharField(max_length=10, unique=True, verbose_name="Государственный номер")
    brand = models.CharField(max_length=100, verbose_name="Марка")
    vin = models.CharField(max_length=17, unique=True, verbose_name="ВИН")
    user = models.ForeignKey('User', related_name='cars', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
