from backend_mercos.models.usuario import Usuario
from backend_mercos.models.pedido import Pedido as PedidoModel
from backend_mercos.models.produto import Produto
from backend_mercos.models.cliente import Cliente
from backend_mercos.models.item_pedido import ItemPedido
from .renderers import UsuarioJSONRenderer, ItemPedidoJSONRenderer, ClienteJSONRenderer, PedidoJSONRenderer, ProdutoJSONRenderer
from .serializers import UsuarioListSerializer, UsuarioSerializer, UsuarioSerializerCadastro, PedidoListSerializer, PedidoDetail
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

'''
####
Usuario
####
'''

class UsuarioGetAll(APIView):
    """
    GET: Retorna a lista de todos os usuários cadastrados no sistema
    POST: Cria um usuário novo
    """

    def get(self, request, format=None):
        usuarios = Usuario.objects.all()
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
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Usuario = self.get_object(pk)
        serializer = UsuarioSerializer(Usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Usuario = self.get_object(pk)
        serializer = UsuarioSerializer(Usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Usuario = self.get_object(pk)
        Usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
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
