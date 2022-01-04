from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from django import forms 
from django.db import transaction
from .models import *


class CreateClientForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {"username": None,
                      "email": None,
                      "password2": None
                      }

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")

        if User.objects.filter(email=email).exists():
            raise ValidationError("User having this email already exists.")

        return self.cleaned_data


    @transaction.atomic  
    def save(self):
        user = super().save(commit=False) 
        user.is_client = True  
        user.is_admin = False
        user.save()  
        return user



class CreateAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {"username": None,
                      "email": None,
                      "password2": None
                      }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.is_client = False
        user.is_staff = True
        user.save()
        return user



class ImageUploadForm(forms.Form):
    image = forms.ImageField()