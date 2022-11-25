from django.forms import ModelForm
from . models import *


class RegisterForm(ModelForm):
    class Meta:
        model = RegisterModel
        fields=['fullname','username','email','password','confirm_password','mobile']
