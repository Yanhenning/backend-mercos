from django.db import models
from .pedido import Pedido
from .produto import Produto
from enum import Enum
from backend_mercos.enums_merc import TipoRentabilidade

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidadeProduto = models.BigIntegerField(default=1)
    precoCliente = models.BigIntegerField()
    rentabilidade = models.CharField(max_length=50,
     choices = [(tag, tag.value) for tag in TipoRentabilidade])

    def __str__(self):
        return (self.produto.nome + quantidadeProduto)

    def getRentabilidade(self):
        return self.rentabilidade

    def getPrecoCliente(self):
        return self.precoCliente
