from ..models.item_pedido import ItemPedido as ItemPedidoModel
from ..models.pedido import Pedido as PedidoModel
from ..models.produto import Produto as ProdutoModel
from backend_mercos.enums_merc import TipoRentabilidade

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
