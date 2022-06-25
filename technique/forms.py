from django import forms
from .models import *
from django.contrib.auth.models import User


class UserRegisterModelForm(forms.ModelForm):

    confirm = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['last_name', 'first_name',
                  'username', 'email', 'password', 'confirm']
        widgets = {
            'password': forms.PasswordInput(),
        }


class techniqueForm(forms.ModelForm):
    class Meta:
        model = technique
        fields = '__all__'


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    age = forms.IntegerField()

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }
