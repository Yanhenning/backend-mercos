from django.test import TestCase
from django.urls import reverse,include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from ..models.cliente import Cliente
from ..serializers import ClienteSerializer

class ClienteTest(APITestCase):
    def setUp(self):
        Cliente.objects.create(id=1, nome="BB-8")
        Cliente.objects.create(id=2, nome="R2-D2")

    def test_dadoCliente_quandoBuscarId_entaoEncontrado(self):
        url = reverse('cliente_id', kwargs={'pk':1})

        serializer = ClienteSerializer(Cliente.objects.get(id=1))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)

    def test_dadoCliente_quandoBuscarId_entaoNaoEncontrado(self):
        url = reverse('cliente_id', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_dadoCliente_quandoCriarCliente_entaoClienteCriado(self):
        url = reverse('cliente')
        data = {
        "nome": "C3-PO"
    }
        serializer = ClienteSerializer(Cliente.objects.get(id=1))
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.get(nome=data['nome']).nome, data['nome'])

    def test_dadoClientes_quandoBuscarTodos_entaoEncontrados(self):
        url = reverse('cliente')

        serializer = ClienteSerializer(Cliente.objects.all(), many=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)
