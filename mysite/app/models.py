from django.db import models


# from django.utils import timezone
# from datetime import datetime, date

class Admin(models.Model):
    company_name = models.CharField(max_length=25, blank=False, null=False)
    name = models.CharField(max_length=25, blank=False, null=False)
    surname = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField(max_length=25, blank=False, null=False)
    password = models.CharField(max_length=25, blank=False, null=False)


class Employee(models.Model):
    # id = models.BigAutoField(primary_key = True)
    # startdate=models.DateField(auto_now_add=False, auto_now=False, blank=True)
    # company = models.ForeignKey(Admin)
    admins = models.ManyToManyField(Admin)
    annual_leave = models.IntegerField()
    name = models.CharField(max_length=25, blank=False, null=False)
    surname = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField(max_length=25, blank=False, null=False)
    password = models.CharField(max_length=25, blank=False, null=False)
    employee_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=25, blank=False, null=False)
    tckn = models.IntegerField()
    birth_date = models.DateField(max_length=25, blank=False, null=False)
    start_date = models.DateField(max_length=25, blank=False, null=False)

    def __str__(self):  # ????????????????
        return self.name


class AnnualLeaveForm(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)  # default=none
    reason = models.CharField(max_length=25, blank=False, null=False)
    annual_leave = models.IntegerField()


class OldForm(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)  # default=none
    reason = models.CharField(max_length=25, blank=False, null=False)
    annual_leave = models.IntegerField()
