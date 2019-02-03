from ..models.cliente import Cliente as ClienteModel
from ..models.pedido import Pedido as PedidoModel
from ..services.item_pedido_service import getAllByPedidoId
from backend_mercos.enums_merc import TipoRentabilidade

from django.http import Http404

def getById(id):
            try:
                return PedidoModel.objects.get(id=id)
            except PedidoModel.DoesNotExist:
                raise Http404

def getAll():
    return PedidoModel.objects.all()

def atualizerPedido(pedido, itemPedido):
    pedido.valor += itemPedido.receita
    pedido.quantidadeItem += itemPedido.quantidadeProduto
    pedido.rentabilidade = itemPedido.rentabilidade
    pedido.save()

def getAllByUsuarioId(usuario_id):
    try:
        return PedidoModel.objects.filter(usuario__id=usuario_id)
    except PedidoModel.DoesNotExist:
        raise Http404

def atualizarRentabilidade(pedido):
    itemPedidos = getAllByPedidoId(pedido.id)
    lucro = 0
    for item in itemPedidos:
        lucro += item['lucro']
    if lucro>=0:
        pedido.rentabilidade = TipoRentabilidade.RO.value
    else:
        pedido.rentabilidade = TipoRentabilidade.RB.value
    pedido.save()
