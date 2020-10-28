from rest_framework import serializers
from apps.modelo.models import Juego,Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['us_mail', 'us_contr']
