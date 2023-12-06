from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
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
