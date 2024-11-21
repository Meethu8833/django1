from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

# class customusercreationform(UserCreationForm):
#     class Meta:
#         model=CustomUser
#         fields=('username','password1','password2','phone_number','address')

class userForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','password1','password2','date_of_birth','profile_picture')
