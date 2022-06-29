from django.views.generic import View, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


from .models import Admin, Employee, AnnualLeaveForm, OldForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# import datetime
# Create your views here.

class SignupView(View):
    def get(self, request):
        return render(request, "company_signup.html")

    def post(self, request):
        company_name = request.POST.get("company_name")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        query = Admin(
            company_name=company_name,
            name=name,
            surname=surname,
            email=email,
            password=password1,
        )

        if password1 == password2:
            query.save()
            return render(request, "company_login.html")

        return render(request, "company_signup.html")  ## burada forma gerek olabilir yine


class CompanyLoginView(View):
    def get(self, request):
        return render(request, "company_login.html")

    def post(self, request):
        name = request.POST.get("name")
        password1 = request.POST.get("password1")

        edit = Admin.objects.get(name=name, password=password1)

        if edit is not None:
            messages.success(request, "Login Success")
            return redirect("main")
        else:
            messages.error(request, "Login Failed")
            return redirect("login")


class CRDEmployeeView(View):
    def get(self, request):
        data = Employee.objects.all()
        context = {"data": data}

        return render(request, "crd_employee.html", context)

    def post(self, request):

        annual_leave = request.POST.get("annual_leave")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        employee_id = request.POST.get("employee_id")
        department = request.POST.get("department")
        tckn = request.POST.get("tckn")
        birth_date = request.POST.get("birth_date")
        start_date = request.POST.get("start_date")

        query = Employee(
            annual_leave=annual_leave,
            name=name,
            surname=surname,
            email=email,
            password=password,
            employee_id=employee_id,
            department=department,
            tckn=tckn,
            birth_date=birth_date,
            start_date=start_date,
        )
        query.save()

        messages.info(request, "Data Inserted Successfully")

        return redirect("personel")


class CompanyUpdateEmployeeView(View):
    def post(self, request):

        annual_leave = request.POST.get("annual_leave")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        employee_id = request.POST.get("employee_id")
        department = request.POST.get("department")
        tckn = request.POST.get("tckn")
        birth_date = request.POST.get("birth_date")
        start_date = request.POST.get("start_date")

        edit = Employee.objects.get(employee_id=employee_id)

        edit.annual_leave = annual_leave,
        edit.name = name,
        edit.surname = surname,
        edit.email = email,
        edit.password = password,
        edit.employee_id = employee_id,
        edit.department = department,
        edit.tckn = tckn,
        edit.birth_date = birth_date,
        edit.start_date = start_date,
        edit.save()

        messages.warning(request, "Data Updates Successfully")

        d = Employee.objects.get(employee_id=employee_id)
        context = {"d": d}

        return redirect("personel")


class CompanyDeleteEmployeeView(View):
    def get(self, request, employee_id):
        d = Employee.objects.get(employee_id=employee_id).delete()

        messages.error(request, "Data Deleted Successfully")

        return redirect("personel")


class EmployeeLoginView(View):
    def get(self, request):
        return render(request, "login_employee.html")

    def post(self, request):
        employee_id = request.POST.get("employee_id")

        edit = Employee.objects.get(employee_id=employee_id)

        if edit is not None:
            return redirect("personelinfo", employee_id)
        else:
            messages.error(request, "Login Failed")
            return redirect("personellogin")


class EmployeeMainView(View):
    def get(self, request, employee_id):
        edit = Employee.objects.get(employee_id=employee_id)
        context = {"edit": edit}

        return render(request, "employee_main_page.html", context)

    def post(self, request, employee_id):
        edit = Employee.objects.get(employee_id=employee_id)
        reason = request.POST.get("reason")
        annual_leave = request.POST.get("annual_leave")
        query = AnnualLeaveForm(employee_id=edit, reason=reason, annual_leave=annual_leave)
        query.save()
        forms = OldForm(employee_id=edit, reason=reason, annual_leave=annual_leave)
        forms.save()

        return redirect("personelinfo", employee_id)


class CompanyMainPageView(View):
    def get(self, request):
        return render(request, "company_main_page.html")


class CompanySetPermissionPageView(View):
    def get(self, request):
        return render(request, "set_permission_page.html")


class CompanyPermissionRequestPageView(View):
    def get(self, request):
        forms = AnnualLeaveForm.objects.all()
        context = {"forms": forms}

        return render(request, "permission_request_page.html", context)


class CompanyUpdatePermissionPageView(View):
    def get(self, request, id):
        edit = AnnualLeaveForm.objects.get(id=id)
        personelold = Employee.objects.get(
            employee_id=edit.employee_id.employee_id
        )

        personelold.annual_leave = personelold.annual_leave - edit.annual_leave
        personelold.save()
        edit.delete()

        return redirect("permissionrequest")


class CompanyDeletePermissionPageView(View):
    def get(self, request, id):
        d = AnnualLeaveForm.objects.get(id=id).delete()

        return redirect("permissionrequest")


class EmployeeOldFormsPageView(View):
    def get(self, request, employee_id):
        oldforms = OldForm.objects.get(employee_id=employee_id)
        context = {"oldforms": oldforms}

        return render(request, "old_forms_page.html", context)


class EmployeeDeleteFormsPageView(View):
    def get(self, request, id):
        d = OldForm.objects.get(id=id).delete()

        return redirect("oldforms", d.employee_id)
