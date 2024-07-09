# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last name')
    email = forms.EmailField(max_length=254, required=True, help_text='Email address')

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        help_text='Campo opcional', 
        label='Nombre',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nombre'}
        )
    )   
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        help_text='Campo opcional',
        label='Apellido',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Apellido'}
        )
    )
    email = forms.EmailField(
        max_length=254, 
        required=True,
        help_text='Campo requerido',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}
        )
    )
    rut = forms.CharField(
        max_length=20,
        required=True,
        label='RUT',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '12345678-9'}
        )
    )
    password1 = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña', 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'rut', 'password1', 'password2')
