# Generated by Django 4.2.7 on 2023-12-05 09:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_orderitem_spare_alter_order_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 12, 20, 23, 203059)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='spare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_item', to='service.spare'),
        ),
    ]
