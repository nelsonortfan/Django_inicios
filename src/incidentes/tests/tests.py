import pytest  
  
from rest_framework.test import APIClient 

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from incidentes.models import IncidenteCorreo
from incidentes.serializers import IncidenteCorreoSerializer

# Create your tests here.

class DjangoTest(APITestCase):

    def setUp(self):
        self.url = reverse('incidentesCorreosLista')

    def test_get_mensaje_correo_list(self):
        response = self.client.get(self.url)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    