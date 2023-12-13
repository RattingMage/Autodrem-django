import subprocess

from django.contrib import admin
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import path
from import_export.admin import ImportExportModelAdmin

from authenticate.models import User, Employee, Car
from authenticate.views import import_sql_data


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(ImportExportModelAdmin):
    list_display = ('license_plate', 'brand', 'vin')
    actions = ['export_to_sql']

    def export_to_sql(self, request, queryset):
        output_file = 'exported_data.sql'
        call_command('dumpdata', 'authenticate.Car', indent=2, output=output_file)

        # Отправка файла на скачивание
        with open(output_file, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/sql')
            response['Content-Disposition'] = 'attachment; filename=exported_data.sql'
            return response

    export_to_sql.short_description = "Export selected to .sql"


urlpatterns = [
    path('import-sql-data/', import_sql_data, name='import_sql_data'),
]