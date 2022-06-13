from django.urls import path

from . import views

urlpatterns = [
	path('bla', views.IndexView.as_view(), name = 'get'),
    path('signup', views.SignupView.as_view(), name = 'get'),
    path('login', views.LoginView.as_view(), name = 'get'),
]