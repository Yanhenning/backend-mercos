from ..models.cliente import Cliente as ClienteModel
from ..models.pedido import Pedido as PedidoModel
from django.http import Http404

def getById(id):
            try:
                return PedidoModel.objects.get(id=id)
            except PedidoModel.DoesNotExist:
                raise Http404
