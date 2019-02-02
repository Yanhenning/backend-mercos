from rest_framework import serializers
from backend_mercos.models.usuario import Usuario
from backend_mercos.models.pedido import Pedido as PedidoModel
from backend_mercos.models.produto import Produto
from backend_mercos.models.cliente import Cliente
from backend_mercos.models.item_pedido import ItemPedido

'''
####
Usuario
####
'''

class UsuarioListSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=200, required = True)
    email = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email')

class UsuarioSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=200, required = True)
    email = serializers.CharField(max_length=50, required=True)
    senha = serializers.CharField(max_length=20, required=True)
    quantidade_pedidos = serializers.CharField(max_length=300,required=False)

    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'senha', 'quantidade_pedidos')

class UsuarioSerializerCadastro(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=200, required = True)
    email = serializers.CharField(max_length=50, required=True)
    senha = serializers.CharField(max_length=20, required=True)
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha')



'''
####
Produto
####
'''
class ProdutoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=200, required = True)
    compra_minima = serializers.CharField(max_length=50, required=True)
    preco = serializers.CharField(max_length=300, required=True)

    class Meta:
        model = Produto
        fields = ('id', 'nome', 'compra_minima', 'preco')


'''
####
Cliente
####
'''
class ClienteSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=200, required = True)

    class Meta:
        model = Cliente
        fields = ('id', 'nome')

'''
####
ItemPedido
####
'''

class ItemPedidoDetail(serializers.ModelSerializer):
    nomeProduto = serializers.CharField(max_length=100, required=True)
    preco = serializers.CharField(max_length=100, required=True)
    precoCliente = serializers.CharField(max_length=100, required=True)
    quantidadeProduto = serializers.CharField(max_length=30, required=True)
    receita = serializers.CharField(max_length=30, required=True)
    lucro = serializers.CharField(max_length=30, required=True)
    rentabilidade = serializers.CharField(source='get_rentabilidade_display')
    multiplo = serializers.CharField(max_length=40)

    class Meta:
        model = ItemPedido
        fields = ('id', 'nomeProduto', 'preco', 'precoCliente' ,'quantidadeProduto', 'receita',
        'lucro', 'rentabilidade', 'multiplo')

'''
####
Pedido
####
'''

class PedidoListSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(max_length=200, required = True)
    quantidadeItem = serializers.CharField(max_length=50, required=True)
    valor = serializers.CharField(max_length=200, required=True)
    rentabilidade = serializers.CharField(source='get_rentabilidade_display')

    class Meta:
        model = PedidoModel
        fields = ('id', 'usuario', 'quantidadeItem', 'valor', 'rentabilidade')

class PedidoDetail(serializers.ModelSerializer):
    usuario = serializers.CharField(max_length=200, required = True)
    cliente = serializers.CharField(max_length=200, required = True)
    quantidadeItem = serializers.CharField(max_length=50, required=True)
    valor = serializers.CharField(max_length=200, required=True)
    rentabilidade = serializers.CharField(source='get_rentabilidade_display')

    class Meta:
        model = PedidoModel
        fields = ('id', 'usuario','cliente', 'quantidadeItem', 'valor', 'rentabilidade')
