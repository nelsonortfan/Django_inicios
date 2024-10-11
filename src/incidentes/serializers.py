from rest_framework import serializers
from incidentes.models import IncidenteCorreo

class IncidenteCorreoSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncidenteCorreo
        fields = '__all__'

    def validate_titulo(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Titulo muy corto')
        else:
            return value
        
