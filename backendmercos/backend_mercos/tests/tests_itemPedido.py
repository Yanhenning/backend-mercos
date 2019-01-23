from django.test import TestCase
from django.urls import reverse,include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from ..models.usuario import Usuario
from ..models.pedido import Pedido
from ..models.item_pedido import ItemPedido
from ..models.produto import Produto
from ..models.cliente import Cliente
from ..serializers import UsuarioListSerializer, UsuarioSerializer, PedidoDetail, PedidoListSerializer, PedidoDetail

class ItemPedidoTest(APITestCase):

    def setUp(self):
        Produto.objects.create(id=1, nome="Millenium​ ​Falcon", compra_minima=0, preco=550000)
        Produto.objects.create(id=2, nome="X-Wing", compra_minima=2, preco=60000)
        Produto.objects.create(id=5, nome="Lightsaber", compra_minima=5, preco=6000)

        cliente1 = Cliente.objects.create(id=1, nome="Darth Vader")
        cliente2 = Cliente.objects.create(id=2, nome="Obi-Wan Kenobi")

        usuario1 = Usuario.objects.create(id=1, nome="Yan Henning", email="yanhenning@gmail.com",senha="111111")
        usuario2 = Usuario.objects.create(id=2, nome="Fred", email="fred@@example.com",senha="222222")

        Pedido.objects.create(id=1, usuario=usuario1, cliente=cliente1)

    def test_dadoProduto_quandoCriarItem_itemCriado(self):
        pedido = Pedido.objects.get(id=1)
        
