from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app import models

admin.site.register(models.PersonelDataBase)
