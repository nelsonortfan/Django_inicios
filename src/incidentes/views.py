from django.http import HttpResponse
from incidentes.models import IncidenteCorreo
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the incidentes index.")


def incidente_correo_lista(request):
    incidentesCorreo = IncidenteCorreo.objects.all()
    print(incidentesCorreo)
    data = {'incidentescorreos': list(incidentesCorreo.values())}
    return JsonResponse(data)
     