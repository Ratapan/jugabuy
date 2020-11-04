from django import forms
from .models import Usuario


# creating a form
class UserForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Usuario

        # specify fields to be used
        fields = [
            "us_rut",
            "us_mail",
            "us_nom",
            "us_apes",
            "us_contr",
            "us_nac",
            "us_creac",
            "us_tel",
            "us_dir",
            "us_sald",
            "id_rol",
            "id_ciud",
        ]
