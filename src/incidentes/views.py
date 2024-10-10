from django.http import HttpResponse
from incidentes.models import IncidenteCorreo
from django.http import JsonResponse
from incidentes.serializers import IncidenteCorreoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hello, world. You're at the incidentes index.")

@api_view()
def incidente_correo_lista(request):
    incidentesCorreo = IncidenteCorreo.objects.all()
    serializer = IncidenteCorreoSerializer(incidentesCorreo, many=True)
    return Response(serializer.data)

@api_view()
def incidente_correo_detalle(request, pk):
    incidente_correo = IncidenteCorreo.objects.get(id=pk)
    serializer = IncidenteCorreoSerializer(incidente_correo)
    return Response(serializer.data)    