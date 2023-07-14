from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto, ContactoReal

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = ['nombre', 'correo', 'mensaje']
        fields='__all__'


class ContactoReal(forms.ModelForm):
    model = ContactoReal
    fields='__all__'