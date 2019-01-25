from ..models.item_pedido import ItemPedido as ItemPedidoModel
from ..models.pedido import Pedido as PedidoModel
from ..models.produto import Produto as ProdutoModel
from backend_mercos.enums_merc import TipoRentabilidade
from django.http import Http404

def calcularRentabilidade(preco, precoCliente):
    if precoCliente > preco:
        return TipoRentabilidade.RO
    if (precoCliente >= (preco - preco*0.10)) & (precoCliente <= preco):
        return TipoRentabilidade.RB
    if precoCliente < (preco - preco*0.10):
        return TipoRentabilidade.RR
    else:
        return TipoRentabilidade.SR

def permitirVendaMultiplo(quantidadeVendaMinima, quantidadeProduto):
    if quantidadeVendaMinima == 0:
        return True
    else:
        if (quantidadeProduto % quantidadeVendaMinima) == 0:
            return True
        else:
            return False

def getById(id):
    try:
        return ItemPedidoModel.objects.get(id=id)
    except ItemPedidoModel.DoesNotExist:
        raise Http404

def getAllByPedidoId(pedido_id):
    return ItemPedidoModel.objects.get(pedido__id=pedido_id)

def calcularLucro(preco, precoCliente, quantidade):
    return ((precoCliente - preco) * quantidade)

def calcularReceita(precoCliente, quantidade):
    return (precoCliente * quantidade)
