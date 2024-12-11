from django import forms
from . models import *

class Normal_Form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    place=forms.CharField()

class Models_Form(forms.ModelForm):
    class Meta:
        model=project_user
        fields='__all__'