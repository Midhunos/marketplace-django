from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product,CustomerDetails


class SignupForm(UserCreationForm):
      class Meta:
            model=User
            fields=('username','email','password1')

class SigninForm(forms.Form):
      username=forms.CharField()
      password=forms.CharField(widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
      class Meta:
            model=Product
            fields='__all__'


class AddressForm(forms.ModelForm):
      class Meta:
            model=CustomerDetails
            fields=('locality','city','street','phono','code')
