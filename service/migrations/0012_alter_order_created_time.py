# Generated by Django 4.2.7 on 2023-12-19 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_order_status_chart_alter_order_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 8, 19, 13, 995725)),
        ),
    ]
