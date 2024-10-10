from django.http import HttpResponse
from incidentes.models import IncidenteCorreo
from django.http import JsonResponse
from incidentes.serializers import IncidenteCorreoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hello, world. You're at the incidentes index.")

@api_view(['GET','POST'])
def incidente_correo_lista(request):
    if request.method == 'GET':
        incidentesCorreo = IncidenteCorreo.objects.all()
        serializer = IncidenteCorreoSerializer(incidentesCorreo, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = IncidenteCorreoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def incidente_correo_detalle(request, pk):
    if request.method == 'GET':
        incidente_correo = IncidenteCorreo.objects.get(id=pk)
        serializer = IncidenteCorreoSerializer(incidente_correo)
        return Response(serializer.data)
    if request.method == 'PUT':
        incidente_correo = IncidenteCorreo.objects.get(id=pk)
        serializer = IncidenteCorreoSerializer(incidente_correo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 

    if request.method == 'DELETE':
        incidente_correo = IncidenteCorreo.objects.get(id=pk)
        incidente_correo.delete()
        return Response("Elemento eliminado correctamente")   