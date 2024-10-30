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
        self.urlIndex = reverse('index')
        self.url = reverse('incidentesCorreosLista')
        self.url2 = reverse('incidenteCorreosDetalle', args=[1])

    def test_get_mensaje_correo_list(self):
        print("El valor de la url es ", self.url)
        response = self.client.get(self.url)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_mensaje_correo_no_existente(self):
        print("El valor de la url2 es ", self.url2)
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_mensaje_correo_no_existente(self):
        print("El valor de la url2 es ", self.url2)
        response = self.client.delete(self.url2)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_url_principal(self):
        response = self.client.get(self.urlIndex)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b"Hello, world. You're at the incidentes index.")




        
    
    