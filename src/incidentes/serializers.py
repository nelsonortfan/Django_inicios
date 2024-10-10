from rest_framework import serializers
from incidentes.models import IncidenteCorreo

class IncidenteCorreoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    titulo = serializers.CharField()
    descripcion = serializers.CharField()
    revisado = serializers.BooleanField()
    correoUsuario = serializers.CharField()
    fechaCreacion = serializers.DateTimeField()

    def create(self, validated_data):
        return IncidenteCorreo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.revisado = validated_data.get('revisado', instance.revisado)
        instance.correoUsuario = validated_data.get('correoUsuario', instance.correoUsuario)
        instance.save()
        return instance
