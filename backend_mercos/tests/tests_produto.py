from django.test import TestCase
from django.urls import reverse,include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from ..models.produto import Produto
from ..serializers import ProdutoSerializer

class ProdutoTest(APITestCase):
    def setUp(self):
        Produto.objects.create(id=1, nome="Stormtrooper Helmet", compra_minima = 1, preco=1000)
        Produto.objects.create(id=2, nome="Death Star Toy", compra_minima = 1, preco=4000)

    def test_dadoProduto_quandoBuscarId_entaoEncontrado(self):
        url = reverse('produto_by_id', kwargs={'id':1})

        serializer = ProdutoSerializer(Produto.objects.get(id=1))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)

    def test_dadoProduto_quandoBuscarId_entaoNaoEncontrado(self):
        url = reverse('produto_by_id', kwargs={'id':99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_dadoProdutos_quandoBuscarTodos_entaoEncontrados(self):
        url = reverse('produto')

        serializer = ProdutoSerializer(Produto.objects.all(), many=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)

class TestProdutoCriado(APITestCase):

    def test_dadoProduto_quandoCriarProduto_entaoProdutoCriado(self):
        url = reverse('produto')
        data = {
        "nome": "Millenium Hawk",
        "compra_minima": "2",
        "preco": "2600"
    }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.get(nome=data['nome']).nome, data['nome'])
