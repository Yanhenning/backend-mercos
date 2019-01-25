from django.test import TestCase
from django.urls import reverse,include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from ..models.usuario import Usuario
from ..models.pedido import Pedido
from ..models.item_pedido import ItemPedido
from ..models.produto import Produto
from ..models.cliente import Cliente
from ..serializers import UsuarioListSerializer, UsuarioSerializer, PedidoDetail, PedidoListSerializer, PedidoDetail, ItemPedidoDetail
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
        Pedido.objects.create(id=2,usuario=usuario2, cliente=cliente2)

    def test_dadoProduto_quandoAdicionarPedido_entaoItemPedidoCriadoRentabilidadeBoa(self):
        url = reverse('item_pedido', kwargs={'id':1})

        produto = Produto.objects.get(id=1)

        data = {'nome_produto':produto.nome,
                    'compra_minima':produto.compra_minima,
                    'preco':produto.preco,
                    'preco_cliente':550000,
                    'quantidade_produto':1
                    }

        response = self.client.post(url, data, format='json')

        serializer = ItemPedidoDetail(ItemPedido.objects.get(id=1))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #TODO fix the serializer from query
        self.assertEqual(response.data['nomeProduto'], produto.nome)
        self.assertEqual(response.data['preco'], str(produto.preco))
        self.assertEqual(response.data['precoCliente'], '550000')
        self.assertEqual(response.data['receita'], str(550000*1))
        self.assertEqual(response.data['lucro'], '0')
        self.assertEqual(response.data['rentabilidade'], TipoRentabilidade.RB.value)

    def test_dadoProduto_quandoAdicionarPedido_entaoItemPedidoCriadoRentabilidadeOtima(self):
        url = reverse('item_pedido', kwargs={'id':1})

        produto = Produto.objects.get(id=1)

        data = {'nome_produto':produto.nome,
                    'compra_minima':produto.compra_minima,
                    'preco':produto.preco,
                    'preco_cliente':550001,
                    'quantidade_produto':1
                    }

        response = self.client.post(url, data, format='json')

        serializer = ItemPedidoDetail(ItemPedido.objects.get(id=1))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #TODO fix the serializer from query
        self.assertEqual(response.data['nomeProduto'], produto.nome)
        self.assertEqual(response.data['preco'], str(produto.preco))
        self.assertEqual(response.data['precoCliente'], '550001')
        self.assertEqual(response.data['receita'], str(550001))
        self.assertEqual(response.data['lucro'], '1')
        self.assertEqual(response.data['rentabilidade'], TipoRentabilidade.RO.value)

    def test_dadoProduto_quandoAdicionarPedidoRentabilidadeRuim_entaoRetornaException(self):
        url = reverse('item_pedido', kwargs={'id':1})

        produto = Produto.objects.get(id=1)

        data = {'nome_produto':produto.nome,
                    'compra_minima':produto.compra_minima,
                    'preco':produto.preco,
                    'preco_cliente':30000,
                    'quantidade_produto':1
                    }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_dadoProduto_quandoCompraMinimaSatisfeita_entaoItemPedidoCriado(self):
        url = reverse('item_pedido', kwargs={'id':1})

        produto = Produto.objects.get(id=2)

        data = {'nome_produto':produto.nome,
                    'compra_minima':produto.compra_minima,
                    'preco':produto.preco,
                    'preco_cliente':60000,
                    'quantidade_produto':8
                    }

        response = self.client.post(url, data, format='json')

        serializer = ItemPedidoDetail(ItemPedido.objects.get(id=1))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #TODO fix the serializer from query
        self.assertEqual(response.data['nomeProduto'], produto.nome)
        self.assertEqual(response.data['preco'], str(produto.preco))
        self.assertEqual(response.data['precoCliente'], '60000')
        self.assertEqual(response.data['receita'], str(60000*8))
        self.assertEqual(response.data['lucro'], '0')
        self.assertEqual(response.data['rentabilidade'], TipoRentabilidade.RB.value)



    def test_dadoProduto_quandoCompraMinimaNaoSatisfeita_entaoItemPedidoNegado(self):
        url = reverse('item_pedido', kwargs={'id':1})

        produto = Produto.objects.get(id=2)

        data = {'nome_produto':produto.nome,
                    'compra_minima':produto.compra_minima,
                    'preco':produto.preco,
                    'preco_cliente':60000,
                    'quantidade_produto':7
                    }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

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
