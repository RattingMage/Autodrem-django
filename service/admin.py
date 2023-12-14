from django.contrib import admin
from django.db.models import Count
from django.templatetags.static import static
from django.urls import path
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from matplotlib import pyplot as plt

from service.models import Spare, Service, Order, RepairRequest


@admin.register(Spare)
class SpareAdmin(ImportExportModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    pass


@admin.register(RepairRequest)
class RepairRequestAdmin(ImportExportModelAdmin):
    pass


# class CustomAdminSite(admin.AdminSite):
#     site_header = 'Администрирование Autodrem'
#
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('order-status-graph/', self.admin_view(self.order_status_graph), name='order_status_graph'),
#         ]
#         return custom_urls + urls
#
#     def order_status_graph(self, request):
#         status_counts = Order.objects.values('status').annotate(count=Count('id'))
#         statuses = [entry['status'] for entry in status_counts]
#         counts = [entry['count'] for entry in status_counts]
#
#         plt.bar(statuses, counts)
#         plt.xlabel('Статус заказа')
#         plt.ylabel('Количество заказов')
#         plt.title('Статистика заказов по статусу')
#
#         image_path = 'C:\\Users\\andre\\Work\\Autodrem\\static\\images\\order_status_graph.png'
#         plt.savefig(image_path)
#         plt.close()
#
#         relative_path = 'images/order_status_graph.png'
#         return format_html('<img src="{}" alt="Order Status Graph">', static(relative_path))
#
#
# admin_site = CustomAdminSite(name='custom_admin')
