from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

class IndexView(View):

	def get(self, request):
		return HttpResponse("fatih naber. you are at the polls index")

class SignupView(View):
    def get(self, request):
        template = loader.get_template('signup.html')
        return HttpResponse( template.render({}, request))

class LoginView(View):
    def get(self, request):
        template = loader.get_template('login.html')
        return HttpResponse( template.render({}, request))

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
