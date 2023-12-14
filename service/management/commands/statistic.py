import os

import matplotlib.pyplot as plt
from django.db.models import Count
from django.core.management.base import BaseCommand

from Autodrem.settings import STATIC_DIR, BASE_DIR
from service.models import Order


class Command(BaseCommand):
    help = 'Get graphic'

    def handle(self, *args, **options):
        status_counts = Order.objects.values('status').annotate(count=Count('id'))

        statuses = [entry['status'] for entry in status_counts]
        counts = [entry['count'] for entry in status_counts]

        plt.bar(statuses, counts)
        plt.xlabel('Статус заказа')
        plt.ylabel('Количество заказов')
        plt.title('Статистика заказов по статусу')

        image_path = os.path.join(BASE_DIR, 'static', 'images', 'order_status_graph.png')
        plt.savefig(image_path)
        plt.close()

        self.stdout.write(self.style.SUCCESS(f'График сохранен в {image_path}'))
