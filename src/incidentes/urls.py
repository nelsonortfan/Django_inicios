from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("incidentesCorreos", views.incidente_correo_lista, name="incidentesCorreosLista"),
    path("<int:pk>", views.incidente_correo_detalle, name="incidenteCorreosDetalle")
]