from django.views.generic import View, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import PersonelDataBase, IzinFormlariDataBase, OldFormsDataBase
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# import datetime
# Create your views here.


class IndexView(View):
    def get(self, request):
        return HttpResponse("fatih naber. you are at the polls index")


class SignupView(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        companyname = request.POST.get("companyname")
        adminnamesurname = request.POST.get("adminnamesurname")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")

        if password != confirmpassword:
            return HttpResponse("Password Incorrect")
        print(companyname, adminnamesurname, password, confirmpassword)

        myuser = User.objects.create_user(adminnamesurname, companyname, password)
        myuser.save()
        
        return render(request, "login.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        adminnamesurname = request.POST.get("adminnamesurname")
        password = request.POST.get("pass1")

        print("adminnamesurname:", adminnamesurname)
        print("password: ", password)

        myuser = authenticate(username=adminnamesurname, password=password)
        print("deneme:", myuser)
        if myuser is not None:
            login(request, myuser)
            print("girdi mi? success")
            messages.success(request, "Login Success")
            print("<adminnamesurname>", adminnamesurname)
            return redirect("main")
        else:
            messages.error(request, "Login Failed")
            print("girdi mi? failed")
            return redirect("login")

        return render(request, "login.html")


class CrudPersonelView(View):
    def get(self, request):
        data = PersonelDataBase.objects.all()
        context = {"data": data}
        # print(context)
        # template = loader.get_template("crudPersonel.html")
        # return HttpResponse(template.render({}, request, context))
        return render(request, "crudPersonel.html", context)

    def post(self, request):

        dayoffs = request.POST.get("dayoffs")
        personelid = request.POST.get("personelid")
        tckn = request.POST.get("tckn")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        sgk = request.POST.get("sgk")
        bloodtype = request.POST.get("bloodtype")
        fathername = request.POST.get("fathername")
        mothername = request.POST.get("mothername")
        status = request.POST.get("status")
        birthplace = request.POST.get("birthplace")
        birthdate = request.POST.get("birthdate")
        province = request.POST.get("province")
        militarystatus = request.POST.get("militarystatus")
        school = request.POST.get("school")
        department = request.POST.get("department")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        address = request.POST.get("address")

        query = PersonelDataBase(
            dayoffs=dayoffs,
            personelid=personelid,
            tckn=tckn,
            name=name,
            surname=surname,
            sgk=sgk,
            bloodtype=bloodtype,
            fathername=fathername,
            mothername=mothername,
            status=status,
            birthplace=birthplace,
            birthdate=birthdate,
            province=province,
            militarystatus=militarystatus,
            school=school,
            department=department,
            telephone=telephone,
            email=email,
            address=address,
        )
        query.save()
        messages.info(request, "Data Inserted Successfully")
        # render redirect("/")

        # template = loader.get_template("crudPersonel.html")

        return redirect("personel")


# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
class UpdateDataView(View):
    def post(self, request, personelid):
        dayoffs = request.POST.get("dayoffs")
        personelid = request.POST.get("personelid")
        tckn = request.POST.get("tckn")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        sgk = request.POST.get("sgk")
        bloodtype = request.POST.get("bloodtype")
        fathername = request.POST.get("fathername")
        mothername = request.POST.get("mothername")
        status = request.POST.get("status")
        birthplace = request.POST.get("birthplace")
        birthdate = request.POST.get("birthdate")
        province = request.POST.get("province")
        militarystatus = request.POST.get("militarystatus")
        school = request.POST.get("school")
        department = request.POST.get("department")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        address = request.POST.get("address")

        edit = PersonelDataBase.objects.get(personelid=personelid)

        edit.dayoffs = dayoffs
        edit.personelid = personelid
        edit.tckn = tckn
        edit.name = name
        edit.surname = surname
        edit.sgk = sgk
        edit.bloodtype = bloodtype
        edit.fathername = fathername
        edit.mothername = mothername
        edit.status = status
        edit.birthplace = birthplace
        edit.birthdate = birthdate
        edit.province = province
        edit.militarystatus = militarystatus
        edit.school = school
        edit.department = department
        edit.telephone = telephone
        edit.email = email
        edit.address = address
        edit.save()

        messages.warning(request, "Data Updates Successfully")

        d = PersonelDataBase.objects.get(personelid=personelid)
        context = {"d": d}
        return redirect("personel")


class DeleteDataView(View):
    def get(self, request, personelid):
        d = PersonelDataBase.objects.get(personelid=personelid)
        d.delete()
        messages.error(request, "Data Deleted Successfully")
        return redirect("personel")


class PersonelLoginView(View):
    def get(self, request):
        return render(request, "loginPersonel.html")

    def post(self, request):
        print("burada misin?")
        personelid = request.POST.get("personelid")

        edit = PersonelDataBase.objects.get(personelid=personelid)
        context = {"edit": edit}

        if edit is not None:
            print("girdi mi? success")
            return redirect("personelinfo", personelid)
        else:
            messages.error(request, "Login Failed")
            return redirect("personellogin")
        return render(request, "loginPersonel.html")


class InfoAndAnnualLeaveView(View):
    def get(self, request, personelid):
        edit = PersonelDataBase.objects.get(personelid=personelid)
        context = {"edit": edit}
        return render(request, "infoAndAnnualLeave.html", context)

    def post(self, request, personelid):
        edit = PersonelDataBase.objects.get(personelid=personelid)
        reason = request.POST.get("reason")
        dayoff = request.POST.get("dayoff")
        query = IzinFormlariDataBase(personelid=edit, reason=reason, dayoff=dayoff)
        query.save()
        forms = OldFormsDataBase(personelid=edit, reason=reason, dayoff=dayoff)
        forms.save()
        return redirect("personelinfo", personelid)


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
        personelold = PersonelDataBase.objects.get(
            personelid=edit.personelid.personelid
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
    def get(self, request, personelid):
        oldforms = OldFormsDataBase.objects.get(personelid=personelid)
        context = {"oldforms": oldforms}
        print(context)
        return render(request, "oldFormsPage.html", context)


class DeleteFormsView(View):
    def get(self, request, id):
        d = OldFormsDataBase.objects.get(id=id)
        d.delete()
        return redirect("oldforms")
