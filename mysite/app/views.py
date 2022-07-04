from django.views.generic import View, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Profile, AdminProfile, EmployeeProfile, IzinFormlariDataBase, OldFormsDataBase
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

        return render(request, "signup.html", {"form": form})

    def post(self, request):
        form = AdminProfileCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "login.html")
        else:
            return HttpResponse("invalid")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        first_name = request.POST.get("first_name")
        password = request.POST.get("pass1")

        print("admin_username:", first_name)
        print("password: ", password)

        myuser = authenticate(username=first_name, password=password)
        if myuser is not None:
            login(request, myuser)
            print("girdi mi? success")
            messages.success(request, "Login Success")
            return redirect("main")
        else:
            messages.error(request, "Login Failed")
            print("girdi mi? failed")
            return redirect("login")


class CrudPersonelView(View):
    def get(self, request):
        data = EmployeeProfile.objects.all()
        context = {"data": data}
        return render(request, "crudPersonel.html", context)

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

        edit = EmployeeProfile.objects.get(employee_id=employee_id)

        edit.username = username
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


class PersonelLoginView(View):
    def get(self, request):
        return render(request, "loginPersonel.html")

    def post(self, request):
        employee_id = request.POST.get("personelid")

        edit = EmployeeProfile.objects.get(employee_id=employee_id)
        context = {"edit": edit}

        if edit is not None:
            return redirect("personelinfo", employee_id)
        else:
            messages.error(request, "Login Failed")
            return redirect("personellogin")
        return render(request, "loginPersonel.html")


class InfoAndAnnualLeaveView(View):
    def get(self, request, employee_id):
        edit = EmployeeProfile.objects.get(employee_id=employee_id)
        context = {"edit": edit}
        return render(request, "infoAndAnnualLeave.html", context)

    def post(self, request, employee_id):
        edit = EmployeeProfile.objects.get(employee_id=employee_id)
        reason = request.POST.get("reason")
        dayoff = request.POST.get("dayoff")
        query = IzinFormlariDataBase(employee_id=edit, reason=reason, dayoff=dayoff)
        query.save()
        forms = OldFormsDataBase(employee_id=edit, reason=reason, dayoff=dayoff)
        forms.save()
        return redirect("personelinfo", employee_id)


class CompanyMainPageView(View):
    def get(self, request):

        return render(request, "companyMainPage.html")


class SetPermissionView(View):
    def get(self, request):
        return render(request, "setPermission.html")


class PermissionRequestView(View):
    def get(self, request):
        forms = IzinFormlariDataBase.objects.all()
        context = {"forms": forms}
        return render(request, "permissionRequest.html", context)


class UpdatePermissionView(View):
    def get(self, request, id):
        edit = IzinFormlariDataBase.objects.get(id=id)
        personelold = EmployeeProfile.objects.get(
            employee_id=edit.employee_id.employee_id
        )
        personelold.dayoffs = personelold.dayoffs - edit.dayoff
        personelold.save()
        edit.delete()
        return redirect("permissionrequest")


class DeletePermissionView(View):
    def get(self, request, id):
        d = IzinFormlariDataBase.objects.get(id=id)
        d.delete()
        return redirect("permissionrequest")


class OldFormsPageView(View):
    def get(self, request, employee_id):
        oldforms = OldFormsDataBase.objects.get(employee_id=employee_id)
        context = {"oldforms": oldforms}
        print(context)
        return render(request, "oldFormsPage.html", context)


class DeleteFormsView(View):
    def get(self, request, id):
        d = OldFormsDataBase.objects.get(id=id)
        d.delete()
        return redirect("oldforms")


class LogoutView(View):
    def get(self, request):
        logout(request)
    # Redirect to a success page.
