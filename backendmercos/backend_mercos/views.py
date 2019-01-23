from backend_mercos.models.usuario import Usuario as UsuarioModel
from backend_mercos.models.pedido import Pedido as PedidoModel
from backend_mercos.models.produto import Produto as ProdutoModel
from backend_mercos.models.cliente import Cliente as ClienteModel
from backend_mercos.models.item_pedido import ItemPedido as ItemPedidoModel
from .renderers import UsuarioJSONRenderer, ItemPedidoJSONRenderer, ClienteJSONRenderer, PedidoJSONRenderer, ProdutoJSONRenderer
from .serializers import UsuarioListSerializer, UsuarioSerializer, UsuarioSerializerCadastro, PedidoListSerializer, PedidoDetail, ClienteSerializer, ProdutoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        usuarios = UsuarioModel.objects.all()
        serializer = UsuarioListSerializer(usuarios,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializerCadastro(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
    """
    GET: retorna o usuário por id
    PUT: cadastra o usuário
    DELETE: deleta o usuário pelo id
    """
    def get_object(self, pk):
        try:
            return UsuarioModel.objects.get(pk=pk)
        except UsuarioModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
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
    """
    def get(self, request, format=None):
        produtos = ProdutoModel.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

class ProdutoById(APIView):
    """
    GET: Retorna o produto com o id
    """
    def get_object(self, pk):
        try:
            return ProdutoModel.objects.get(pk=pk)
        except ProdutoModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        produto = self.get_object(pk)
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
        clientes = ClienteModel.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

class ClienteById(APIView):
    """
    GET: Retorna o cliente com o id
    """
    def get_object(self, pk):
        try:
            return ClienteModel.objects.get(pk=pk)
        except ClienteModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)


'''
####
ItemPedido
####
'''





'''
####
Pedido
####
'''
class Pedido(APIView):
    '''
    GET: Retonar todos os pedidos criados
    POST: Criar um Pedido
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
    def get_object(self, pk):
        try:
            return PedidoModel.objects.get(pk=pk)
        except PedidoModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serializer = PedidoDetail(pedido)
        return Response(serializer.data)
