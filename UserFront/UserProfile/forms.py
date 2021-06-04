from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms.widgets import PasswordInput, Widget

from .models import userProfile #Using the userProfile that we created in models.py

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
#To create a form for Username, Email and Password
class AuthenticatingElements(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput())
    class Meta():
        model = User
        fields = ["username","email","password"]


#To create a form for Name and Phone Number Elements
class MoreElements(forms.ModelForm):
    phoneNumber = PhoneNumberField(widget = PhoneNumberPrefixWidget(initial="IN"))
    class Meta():
        model = userProfile
        fields = ["name","phoneNumber"]