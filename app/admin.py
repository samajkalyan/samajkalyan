from django.contrib import admin
from app.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(FormData)


@admin.register(FormData)
class ViewAdmin(ImportExportModelAdmin):
    pass