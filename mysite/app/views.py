from django.views.generic import View, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Profile, AdminProfile, EmployeeProfile, AnnualLeaveForm, OldFormsDataBase
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import AdminProfileCreationForm
from django.contrib.auth import logout


# import datetime
# Create your views here.

class SignupView(View):
    def get(self, request):
        form = AdminProfileCreationForm

        return render(request, "company_signup.html", {"form": form})

    def post(self, request):
        form = AdminProfileCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "company_login.html")
        else:
            return HttpResponse("invalid")


class CompanyLoginView(View):
    def get(self, request):
        return render(request, "company_login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password1")

        myuser = authenticate(username=username, password=password)
        print(myuser)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect("main")
        else:
            messages.error(request, "Login Failed")
            return redirect("login")


class CRDEmployeeView(View):
    def get(self, request):
        data = EmployeeProfile.objects.all()
        context = {"data": data}
        return render(request, "crd_employee.html", context)

    def post(self, request):
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        annual_leave = request.POST.get("annual_leave")
        employee_id = request.POST.get("employee_id")
        department = request.POST.get("department")
        tckn = request.POST.get("tckn")
        birth_date = request.POST.get("birth_date")
        start_date = request.POST.get("start_date")

        query = EmployeeProfile(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            annual_leave=annual_leave,
            employee_id=employee_id,
            department=department,
            tckn=tckn,
            birth_date=birth_date,
            start_date=start_date,
        )
        query.save()
        messages.info(request, "Data Inserted Successfully")

        return redirect("personel")


class UpdateDataView(View):
    def post(self, request, employee_id):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        annual_leave = request.POST.get("annual_leave")
        employee_id = request.POST.get("employee_id")
        department = request.POST.get("department")
        tckn = request.POST.get("tckn")
        birth_date = request.POST.get("birth_date")
        start_date = request.POST.get("start_date")

        edit = EmployeeProfile.objects.get(employee_id=employee_id)

        edit.first_name = first_name
        edit.last_name = last_name
        edit.email = email
        edit.password = password
        edit.annual_leave = annual_leave
        edit.employee_id = employee_id
        edit.department = department
        edit.tckn = tckn
        edit.birth_date = birth_date
        edit.start_date = start_date

        edit.save()

        messages.warning(request, "Data Updates Successfully")

        d = EmployeeProfile.objects.get(employee_id=employee_id)
        context = {"d": d}

        return redirect("personel")


class DeleteDataView(View):
    def get(self, request, employee_id):
        d = EmployeeProfile.objects.get(employee_id=employee_id)
        d.delete()
        messages.error(request, "Data Deleted Successfully")

        return redirect("personel")


class EmployeeLoginView(View):
    def get(self, request):
        return render(request, "login_employee.html")

    def post(self, request):
        employee_id = request.POST.get("employee_id")

        edit = EmployeeProfile.objects.get(employee_id=employee_id)
        context = {"edit": edit}
        print("edit: ", edit)

        if edit is not None:
            return redirect("personelinfo", employee_id)
        else:
            messages.error(request, "Login Failed")
            return redirect("personellogin")


class InfoAndAnnualLeaveView(View):
    def get(self, request, employee_id):
        edit = EmployeeProfile.objects.get(employee_id=employee_id)
        context = {"edit": edit}
        return render(request, "employee_main_page.html", context)

    def post(self, request, employee_id):
        edit = EmployeeProfile.objects.get(employee_id=employee_id)
        reason = request.POST.get("reason")
        annual_leave = request.POST.get("annual_leave")
        query = AnnualLeaveForm(employee_id=edit, reason=reason, annual_leave=annual_leave)
        query.save()
        forms = OldFormsDataBase(employee_id=edit, reason=reason, annual_leave=annual_leave)
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
        personelold = EmployeeProfile.objects.get(
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


class OldFormsPageView(View):
    def get(self, request, employee_id):
        oldforms = OldFormsDataBase.objects.get(employee_id=employee_id)
        context = {"oldforms": oldforms}

        return render(request, "old_forms_page.html", context)


class EmployeeDeleteFormsPageView(View):
    def get(self, request, id):
        d = OldFormsDataBase.objects.get(id=id)
        d.delete()
        return redirect("oldforms")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
    # Redirect to a success page.
