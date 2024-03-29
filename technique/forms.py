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


class TechniqueForm(forms.ModelForm):
    class Meta:
        model = Technique
        fields = '__all__'


# class AksiyaForm(forms.ModelForm):
#     class Meta:
#         model = Aksiya
#         fields = '__all__'


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }
