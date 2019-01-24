from ..models.cliente import Cliente as ClienteModel
from ..models.pedido import Pedido as PedidoModel
from django.http import Http404

def getById(id):
            try:
                return PedidoModel.objects.get(id=id)
            except PedidoModel.DoesNotExist:
                raise Http404

def getAll():
    return PedidoModel.objects.all()


def getAllByUsuarioId(usuario_id):
    try:
        return PedidoModel.objects.filter(usuario__id=usuario_id)
    except PedidoModel.DoesNotExist:
        raise Http404
