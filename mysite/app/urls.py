from django.urls import path

from . import views

urlpatterns = [
    path("bla", views.IndexView.as_view(), name="get"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("personel", views.CrudPersonelView.as_view(), name="personel"),

    path("update/<id>", views.UpdateDataView.as_view(), name="post"),
    path("delete/<id>", views.DeleteDataView.as_view(), name="post"),

    
]
