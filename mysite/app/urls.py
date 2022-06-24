from django.urls import path

from . import views

urlpatterns = [
    path("bla", views.IndexView.as_view(), name="get"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("personel", views.CrudPersonelView.as_view(), name="personel"),

    path("update/<personelid>", views.UpdateDataView.as_view(), name="update"),
    path("delete/<personelid>", views.DeleteDataView.as_view(), name="delete"),

    path("personellogin", views.PersonelLoginView.as_view(), name="personellogin"),
    path("personelinfo/<personelid>", views.InfoAndAnnualLeaveView.as_view(), name="personelinfo"),
    path("main", views.CompanyMainPageView.as_view(), name="main"),
    path("setpermission", views.SetPermissionView.as_view(), name="setpermission"),
    path("permissionrequest", views.PermissionRequestView.as_view(), name="permissionrequest"),
    path("deleterequest/<id>", views.DeletePermissionView.as_view(), name="deleterequest"),
    path("acceptrequest/<id>", views.UpdatePermissionView.as_view(), name="acceptrequest"),
    path("oldforms/<personelid>", views.OldFormsPageView.as_view(), name="oldforms"),
    path("deleteform/<id>", views.DeleteFormsView.as_view(), name="deleteforms"),

    
]
