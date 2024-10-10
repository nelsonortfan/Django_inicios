from rest_framework import serializers

class IncidenteCorreoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    titulo = serializers.CharField()
    descripcion = serializers.CharField()
    revisado = serializers.BooleanField()
    correoUsuario = serializers.CharField()
    fechaCreacion = serializers.DateTimeField()
