from django.views.generic import View, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import PersonelDataBase
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


class IndexView(View):
    def get(self, request):
        return HttpResponse("fatih naber. you are at the polls index")


class SignupView(View):
    def get(self, request):
        return render(request, "signup.html")
    def post(self, request):
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        if(password!=confirmpassword):
            return HttpResponse("Password Incorrect")
        print(uname, email, password, confirmpassword)
        myuser=User.objects.create_user(uname, email, password)
        myuser.save()
        return render(request, "login.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        print("lol")
        username=request.POST.get("username")
        pass1=request.POST.get("pass1")

        myuser=authenticate(uname=username, password = pass1)

        print(myuser)
        
        if myuser is not None:
            login(request, myuser) 
            print("girdi mi? success")
            messages.success(request, "Login Success")
            return redirect("personel")
        else:
            messages.error(request, "Login Failed")
            print("girdi mi? failed")
            return redirect("login")
        
        return render(request, "login.html")

class CrudPersonelView(View):
    def get(self, request):
        data=PersonelDataBase.objects.all()
        context={"data": data}
        #print(context)
        #template = loader.get_template("crudPersonel.html")
        #return HttpResponse(template.render({}, request, context))
        return render(request, "crudPersonel.html", context)

    def post(self, request):  

        personelid=request.POST.get('personelid')
        tckn=request.POST.get('tckn')
        name= request.POST.get('name')
        surname= request.POST.get('surname')
        sgk=request.POST.get('sgk')
        bloodtype= request.POST.get('bloodtype')
        fathername= request.POST.get('fathername')
        mothername= request.POST.get('mothername')
        status= request.POST.get('status')
        birthplace= request.POST.get('birthplace')
        birthdate= request.POST.get('birthdate')
        province= request.POST.get('province')
        militarystatus= request.POST.get('militarystatus')
        school= request.POST.get('school')
        department= request.POST.get('department')
        telephone=request.POST.get('telephone')
        email= request.POST.get('email')
        address= request.POST.get('address')

        

        query=PersonelDataBase(personelid=personelid, tckn=tckn, name=name, surname=surname, sgk=sgk, bloodtype=bloodtype, fathername=fathername, mothername=mothername, status=status, birthplace=birthplace, birthdate=birthdate, province=province, militarystatus=militarystatus, school=school, department=department, telephone=telephone, email=email, address=address)
        query.save()
        messages.info(request, "Data Inserted Successfully")
        #render redirect("/") 

        #template = loader.get_template("crudPersonel.html")
        return redirect("personel") 

# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
class UpdateDataView(View):
    def post(self, request, id):
        personelid=request.POST.get('personelid')
        tckn=request.POST.get('tckn')
        name= request.POST.get('name')
        surname= request.POST.get('surname')
        sgk=request.POST.get('sgk')
        bloodtype= request.POST.get('bloodtype')
        fathername= request.POST.get('fathername')
        mothername= request.POST.get('mothername')
        status= request.POST.get('status')
        birthplace= request.POST.get('birthplace')
        birthdate= request.POST.get('birthdate')
        province= request.POST.get('province')
        militarystatus= request.POST.get('militarystatus')
        school= request.POST.get('school')
        department= request.POST.get('department')
        telephone=request.POST.get('telephone')
        email= request.POST.get('email')
        address= request.POST.get('address')

        edit=PersonelDataBase.objects.get(id=id)

        edit.personelid=personelid
        edit.tckn=tckn
        edit.name=name
        edit.surname=surname
        edit.sgk=sgk
        edit.bloodtype=bloodtype
        edit.fathername=fathername
        edit.mothername=mothername
        edit.status=status
        edit.birthplace=birthplace
        edit.birthdate=birthdate
        edit.province=province
        edit.militarystatus=militarystatus
        edit.school=school
        edit.department=department
        edit.telephone=telephone
        edit.email=email
        edit.address=address
        edit.save()
        
        messages.warning(request, "Data Updates Successfully")

        d=PersonelDataBase.objects.get(id=id)
        context={"d": d}
        return redirect("personel") 

class DeleteDataView(View):
    def get(self, request, id):
        d=PersonelDataBase.objects.get(id=id)
        d.delete()
        messages.error(request, "Data Deleted Successfully")
        return redirect("personel")


