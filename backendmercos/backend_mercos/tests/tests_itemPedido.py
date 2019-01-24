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
from ..services.item_pedido_service import calcularRentabilidade, permitirVendaMultiplo
from backend_mercos.enums_merc import TipoRentabilidade
from ..services import item_pedido_service as itemPedidoService

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

class ItemPedidoService(APITestCase):

    def test_dadoItemPedido_quandoCalcularRentabilidade_rentabilidadeOtima(self):
        preco = 100
        preco_cliente = 100.1
        rentabilidade = itemPedidoService.calcularRentabilidade(preco, preco_cliente)
        self.assertEqual(TipoRentabilidade.RO, rentabilidade)

    def test_precocliente10Abaixo_quandoCalcularRentabilidade_rentabilidadeBoa(self):
        preco = 100
        preco_cliente = 90
        rentabilidade = itemPedidoService.calcularRentabilidade(preco, preco_cliente)
        self.assertEqual(TipoRentabilidade.RB, rentabilidade)

    def test_precoclienteIgualPrecoProduto_quandoCalcularRentabilidade_rentabilidadeBoa(self):
        preco = 100
        preco_cliente = 100
        rentabilidade = itemPedidoService.calcularRentabilidade(preco, preco_cliente)
        self.assertEqual(TipoRentabilidade.RB, rentabilidade)

    def test_precoclienteMenor10PerctPrecoProduto_quandoCalcularRentabilidade_rentabilidadeBoa(self):
        preco = 100
        preco_cliente = 89.9
        rentabilidade = itemPedidoService.calcularRentabilidade(preco, preco_cliente)
        self.assertEqual(TipoRentabilidade.RR, rentabilidade)

    def test_dadoProdutoSemCompraMinima_quandoQualquerQuantidade_entaoProdutoCompravel(self):
        compra_minima = 0
        quantidade_cliente = 2
        permitir_compra = itemPedidoService.permitirVendaMultiplo(compra_minima, quantidade_cliente)
        self.assertEqual(permitir_compra, True)

    def test_dadoProdutoCompraMinima_quandoQuantidadeMultiplo_entaoProdutoCompravel(self):
        compra_minima = 5
        quantidade_cliente = 15
        permitir_compra = itemPedidoService.permitirVendaMultiplo(compra_minima, quantidade_cliente)
        self.assertEqual(permitir_compra, True)

    def test_dadoProdutoCompraMinima_quandoQuantidadeErrada_entaoProdutoCompravel(self):
        compra_minima = 2
        quantidade_cliente = 3
        permitir_compra = itemPedidoService.permitirVendaMultiplo(compra_minima, quantidade_cliente)
        self.assertEqual(permitir_compra, False)
