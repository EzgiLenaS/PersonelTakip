from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    company_name = models.CharField(max_length=25, blank=False, null=False)
    city_name = models.CharField(max_length=25, blank=False, null=False)


class AdminProfile(Profile):
    admin_id = models.IntegerField(primary_key=True)


class EmployeeProfile(Profile):
    # id = models.BigAutoField(primary_key = True)
    annual_leave = models.IntegerField()
    employee_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=25, blank=False, null=False)
    tckn = models.IntegerField()
    birth_date = models.DateField(max_length=25, blank=False, null=False)
    start_date = models.DateField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name


class IzinFormlariDataBase(models.Model):
    employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)  # default=none
    reason = models.CharField(max_length=25, blank=False, null=False)
    dayoff = models.IntegerField()


class OldFormsDataBase(models.Model):
    employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)  # default=none
    reason = models.CharField(max_length=25, blank=False, null=False)
    dayoff = models.IntegerField()
