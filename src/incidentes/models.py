from django.db import models

# Create your models here.

class IncidenteCorreo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    revisado = models.BooleanField(default=False)
    correoUsuario = models.CharField(max_length=20)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class Incidente(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    numeroDocumento = models.IntegerField()
    tipoDocumento = models.TextField()
    nombreUsuario = models.CharField(max_length=100)
    empresaAsociada = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    planEmpresarial = models.CharField(max_length=100)
