from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from .models import UserAccount

def validate_email(value):
    if UserAccount.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken."),params = {'value':value})
    
def validate_phone(value):
    if UserAccount.objects.filter(phone = value).exists():
        raise ValidationError((f"{value} is taken."),params = {'value':value})
    if value < 1000000000 or value > 9999999999:
        raise ValidationError((f"{value} is Invalid."),params = {'value':value})

class SignupForm(UserCreationForm):
    email = forms.EmailField(validators = [validate_email])
    phone = forms.IntegerField(validators = [validate_phone])
    class Meta:
        model = UserAccount
        fields = [
            'username',
            'email',
            'phone',
            'password1',
            'password2'
        ]   


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(validators = [validate_email])
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]   