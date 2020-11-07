from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import perfil


class PerfilForm(ModelForm):
    class Meta:
        model = perfil
        fields = [
        "nom_user",
        "us_rut",
        "us_mail",
        "us_nom",
        "us_apes",
        "us_nac",
        "us_creac",
        "us_tel",
        "us_dir",
        "us_sald",
        "id_rol",
        "id_ciud"
    ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

