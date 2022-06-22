from django import forms
from django.forms import ModelForm




class DateInput(forms.DateInput):
    input_type = 'date'


class PromiseForm(ModelForm):

    class Meta:
        
        fields = ['made_on']
        widgets = {
            'made_on': DateInput(),
        }