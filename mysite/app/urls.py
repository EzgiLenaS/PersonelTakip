from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("personel", views.CrudPersonelView.as_view(), name="personel"),

    path("update/<employee_id>", views.UpdateDataView.as_view(), name="update"),
    path("delete/<employee_id>", views.DeleteDataView.as_view(), name="delete"),

    path("personellogin", views.PersonelLoginView.as_view(), name="personellogin"),
    path("personelinfo/<employee_id>", views.InfoAndAnnualLeaveView.as_view(), name="personelinfo"),
    path("main", views.CompanyMainPageView.as_view(), name="main"),
    path("setpermission", views.SetPermissionView.as_view(), name="setpermission"),
    path("permissionrequest", views.PermissionRequestView.as_view(), name="permissionrequest"),
    path("deleterequest/<id>", views.DeletePermissionView.as_view(), name="deleterequest"),
    path("acceptrequest/<id>", views.UpdatePermissionView.as_view(), name="acceptrequest"),
    path("oldforms/<employee_id>", views.OldFormsPageView.as_view(), name="oldforms"),
    path("deleteform/<id>", views.DeleteFormsView.as_view(), name="deleteforms"),
    path("logout", views.LogoutView.as_view(), name="logout"),

]
