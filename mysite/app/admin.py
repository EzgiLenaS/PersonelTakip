from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from app import models
from .forms import AdminProfileCreationForm


class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(models.AdminProfile)
admin.site.register(models.EmployeeProfile)
admin.site.register(models.AnnualLeaveForm)
admin.site.register(models.OldFormsDataBase)
# admin.site.register(models.MyUsers)
