from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app import models

admin.site.register(models.PersonelDataBase)
admin.site.register(models.IzinFormlariDataBase)
admin.site.register(models.OldFormsDataBase)
#admin.site.register(models.MyUsers)
