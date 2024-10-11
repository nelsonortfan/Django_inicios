from django.http import HttpResponse
from incidentes.models import IncidenteCorreo
from django.http import JsonResponse
from incidentes.serializers import IncidenteCorreoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def index(request):
    return HttpResponse("Hello, world. You're at the incidentes index.")

@api_view(['GET','POST'])
def incidente_correo_lista(request):
    if request.method == 'GET':
        incidentesCorreo = IncidenteCorreo.objects.all()
        serializer = IncidenteCorreoSerializer(incidentesCorreo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = IncidenteCorreoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def incidente_correo_detalle(request, pk):
    if request.method == 'GET':
        try:
            incidente_correo = IncidenteCorreo.objects.get(id=pk)
        except IncidenteCorreo.DoesNotExist:
            return Response({'error':'Correo con Incidente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IncidenteCorreoSerializer(incidente_correo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        try:
            incidente_correo = IncidenteCorreo.objects.get(id=pk)
        except IncidenteCorreo.DoesNotExist:
            return Response({'error':'Correo con Incidente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IncidenteCorreoSerializer(incidente_correo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    if request.method == 'DELETE':
        try:
            incidente_correo = IncidenteCorreo.objects.get(id=pk)
        except IncidenteCorreo.DoesNotExist:
            return Response({'error':'Correo con Incidente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        incidente_correo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   