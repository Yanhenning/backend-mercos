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
from backend_mercos.enums_merc import TipoRentabilidade
from ..services import pedido_service as pedidoService
from rest_framework.exceptions import ValidationError

class PedidoTest(APITestCase):

    def setUp(self):
        Produto.objects.create(id=1, nome="Millenium​ ​Falcon", compra_minima=0, preco=550000)
        Produto.objects.create(id=2, nome="X-Wing", compra_minima=2, preco=60000)
        Produto.objects.create(id=5, nome="Lightsaber", compra_minima=5, preco=6000)

        cliente1 = Cliente.objects.create(id=1, nome="Darth Vader")
        cliente2 = Cliente.objects.create(id=2, nome="Obi-Wan Kenobi")

        usuario1 = Usuario.objects.create(id=1, nome="Yan Henning", email="yanhenning@gmail.com",senha="111111")
        usuario2 = Usuario.objects.create(id=2, nome="Fred", email="fred@example.com",senha="222222")


    def test_dadoPedidos_quandoBuscarPedidosUsuario_entaoPedidosEncontrados(self):
        url = reverse('pedidos_cliente', kwargs={'id':1})
        usuario = Usuario.objects.get(id=1)
        usuario2 = Usuario.objects.get(id=2)
        cliente = Cliente.objects.get(id=1)

        pedidos = []

        pedidos.append(Pedido.objects.create(id=1,usuario=usuario, cliente=cliente))
        Pedido.objects.create(id=2,usuario=usuario2, cliente=cliente)
        pedidos.append(Pedido.objects.create(id=3,usuario=usuario, cliente=cliente))

        serializer = PedidoDetail(pedidos, many=True)

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 2)

    def test_dadoUsuario_quandoCriarPedido_entaoPedidoCriado(self):
        url = reverse('pedidos_cliente', kwargs={'id':1})
        data = {'cliente_id':2}
        response = self.client.post(url, data, format='json')

        usuario = Usuario.objects.get(id=1)

        cliente = Cliente.objects.get(id=data['cliente_id'])

        pedido = Pedido.objects.create(usuario=usuario, cliente=cliente, rentabilidade=TipoRentabilidade.SR)

        serializer = PedidoDetail(pedido)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['usuario'], serializer.data['usuario'])
        self.assertEqual(response.data['cliente'], serializer.data['cliente'])
        self.assertEqual(response.data['rentabilidade'], serializer.data['rentabilidade'])

    def test_dadoUsuario_quandoCriarPedidoDadosInvalidos_entaoRetornaValidationError(self):
        url = reverse('pedidos_cliente', kwargs={'id':1})
        data = {'clienteid':2}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class PedidoServiceTest(APITestCase):

    def setUp(self):
        Produto.objects.create(id=1, nome="Millenium​ ​Falcon", compra_minima=0, preco=550000)
        Produto.objects.create(id=2, nome="X-Wing", compra_minima=2, preco=60000)
        Produto.objects.create(id=5, nome="Lightsaber", compra_minima=5, preco=6000)

        cliente1 = Cliente.objects.create(id=1, nome="Darth Vader")
        cliente2 = Cliente.objects.create(id=2, nome="Obi-Wan Kenobi")

        usuario1 = Usuario.objects.create(id=1, nome="Yan Henning", email="yanhenning@gmail.com",senha="111111")
        usuario2 = Usuario.objects.create(id=2, nome="Fred", email="fred@@example.com",senha="222222")

    def test_dadoPedidoService_quandoBuscarPedidosUsuario_entaoPedidosEncontrados(self):

        usuario = Usuario.objects.get(id=1)
        usuario2 = Usuario.objects.get(id=2)
        cliente = Cliente.objects.get(id=1)
        pedidos = []

        pedidos.append(Pedido.objects.create(id=1,usuario=usuario, cliente=cliente))
        Pedido.objects.create(id=2,usuario=usuario2, cliente=cliente)
        pedidos.append(Pedido.objects.create(id=3,usuario=usuario, cliente=cliente))

        pedidosResult = pedidoService.getAllByUsuarioId(1)

        self.assertEqual(list(pedidosResult), pedidos)
