from backend_mercos.models.usuario import Usuario as UsuarioModel
from backend_mercos.models.pedido import Pedido as PedidoModel
from backend_mercos.models.produto import Produto as ProdutoModel
from backend_mercos.models.cliente import Cliente as ClienteModel
from backend_mercos.models.item_pedido import ItemPedido as ItemPedidoModel
from .renderers import UsuarioJSONRenderer, ItemPedidoJSONRenderer, ClienteJSONRenderer, PedidoJSONRenderer, ProdutoJSONRenderer
from .serializers import UsuarioListSerializer, UsuarioSerializer, UsuarioSerializerCadastro, PedidoListSerializer, PedidoDetail, ClienteSerializer, ProdutoSerializer, ItemPedidoDetail
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import item_pedido_service as itemPedidoService
from .services import usuario_service as usuarioService
from .services import produto_service as produtoService
from .services import cliente_service as clienteService
from .services import pedido_service as pedidoService
from backend_mercos.enums_merc import TipoRentabilidade
from rest_framework.exceptions import ValidationError

'''
####
Usuario
####
'''

class Usuario(APIView):
    """
    GET: Retorna a lista de todos os usuários cadastrados no sistema
    POST: Cria um usuário novo
    """

    def get(self, request, format=None):
        usuarios = usuarioService.getAll()
        serializer = UsuarioListSerializer(usuarios,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializerCadastro(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioById(APIView):
    """
    GET: retorna o usuário por id
    PUT: cadastra o usuário
    DELETE: deleta o usuário pelo id
    """

    def get(self, request, id, format=None):
        usuario = usuarioService.getById(id)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        usuario = usuarioService.getById(id)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        usuario = usuarioService.getById(id)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
####
Produto
####
'''
class Produto(APIView):
    """
    GET: Retorna todos os produtos
    POST: Criar um novo produto
    """
    def get(self, request, format=None):
        produtos = produtoService.getAll()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdutoById(APIView):
    """
    GET: Retorna o produto com o id
    """
    def get(self, request, id, format=None):
        produto = produtoService.getById(id)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

'''
####
Cliente
####
'''
class Cliente(APIView):
    """
    GET: Retorna todos os clientes
    """
    def get(self, request, format=None):
        clientes = clienteService.getAll()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteById(APIView):
    """
    GET: Retorna o cliente com o id
    """

    def get(self, request, id, format=None):
        cliente = clienteService.getById(id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

'''
####
ItemPedido
####
'''
class ItemPedido(APIView):
    '''
    GET: Retorna todos os ItemPedido do pedido com o respectivo id
    POST: Criar o ItemPedido no pedido com o respectivo id
    '''

    def get(self, request, id, format=None):
        itemsPedido = itemPedidoService.getAllByPedidoId(id)
        serializer = ItemPedidoDetail(itemsPedido, many=True)
        return Response(serializer.data)

    def post(self, request, id, format=None):

        try:
            data = request.data
            nomeProduto = data['nome_produto']
            preco = data['preco']
            precoCliente = data['preco_cliente']
            quantidade = data['quantidade_produto']
            compraMinima = data['compra_minima']
        except:
            raise ValidationError("Dados inválidos")

        if itemPedidoService.permitirVendaMultiplo(compraMinima, quantidade):
            pedido = pedidoService.getById(id)
            rentabilidade = itemPedidoService.calcularRentabilidade(preco, precoCliente)
            if rentabilidade == TipoRentabilidade.RR:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                item = ItemPedidoModel.objects.create_item(pedido=pedido, nomeProduto=nomeProduto,
                preco=preco,precoCliente=precoCliente,quantidadeProduto=quantidade,
                rentabilidade=rentabilidade)
                pedidoService.atualizerPedido(pedido, item)
                serializer = ItemPedidoDetail(item)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError({"A compra deve ser múltiplo de": compraMinima})

class ItemPedidoById(APIView):
    '''
    GET: Retorna o ItemPedido do respectivo id
    '''

    def get(self, request, id,format=None):
        itemPedido = itemPedidoService.getById(id)
        serializer = ItemPedidoDetail(itemPedido)
        return Response(serializer.data)

'''
####
Pedido
####
'''
class Pedido(APIView):
    '''
    GET: Retona todos os pedidos criados
    '''

    def get(self, request, format=None):
        pedidos = PedidoModel.objects.all()
        serializer = PedidoListSerializer(pedidos, many=True)
        return Response(serializer.data)

class PedidoById(APIView):
    '''
    GET: Retorna o pedido do id com mais informações
    PUT: Edita o pedido pelo id
    DELETE: delete o pedido do id
    '''

    def get(self, request, id, format=None):
        pedido = pedidoService.getById(id)
        serializer = PedidoDetail(pedido)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        pedido = pedidoService.getById(id)

        try:
            cliente_id = request.data['cliente_id']
        except:
            return Response(HTTP_400_BAD_REQUEST)

        pedido.cliente = clienteService.getById(cliente_id)
        pedido.save()
        serializer = PedidoDetail(pedido)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, format=None):
        pedido = pedidoService.getById(id)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PedidoByIdUsuario(APIView):
    '''
    GET: Retorna todos os pedidos do usuario com respectivo id
    '''

    def get(self, request, id, format=None):
        pedido = pedidoService.getAllByUsuarioId(id)
        serializer = PedidoDetail(pedido, many=True)
        return Response(serializer.data)

    def post(self, request, id, format=None):

        try:
            cliente_id = request.data['cliente_id']
        except:
            raise ValidationError

        usuario = usuarioService.getById(id)
        cliente = clienteService.getById(id=cliente_id)

        pedido = PedidoModel.objects.create(usuario=usuario, cliente=cliente,
        rentabilidade=TipoRentabilidade.SR)

        try:
            pedido.save()
            return Response(PedidoDetail(pedido).data, status=status.HTTP_201_CREATED)
        except PedidoModel.DoesNotExist:
            raise Http404
