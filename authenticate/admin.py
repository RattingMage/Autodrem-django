from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from authenticate.models import User, Employee, Car


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(ImportExportModelAdmin):
    pass
