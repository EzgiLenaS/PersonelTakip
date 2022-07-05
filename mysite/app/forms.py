from django import forms
# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class AdminProfileCreationForm(UserCreationForm):

    class Meta:
        model = AdminProfile
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "company_name",
            "city_name",
            "password1",
            "password2",
            "admin_id",
        )


class GeeksForm(forms.Form):
    geeks_field = forms.DateField( )
