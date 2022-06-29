from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app import models

admin.site.register(models.Admin)
admin.site.register(models.Employee)
admin.site.register(models.AnnualLeaveForm)
admin.site.register(models.OldForm)
#admin.site.register(models.MyUsers)
