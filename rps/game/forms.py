from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={"class":"form-control" ,"id":"username", "required":"true", "autocomplete":"false"}))
    password=forms.CharField(label="Password",widget=forms.TextInput(attrs={"type":"password", "class":"form-control", "id":"password", "required":"true"}))

