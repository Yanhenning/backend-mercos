from django.db import models
from .pedido import Pedido
from .produto import Produto
from enum import Enum
from backend_mercos.enums_merc import TipoRentabilidade


class ItemPedidoManager(models.Manager):
    def create_item(self, pedido, nomeProduto, preco, precoCliente, quantidadeProduto, rentabilidade):
        itemPedido = self.create(pedido=pedido, nomeProduto=nomeProduto,quantidadeProduto=quantidadeProduto,
         preco=preco, precoCliente=precoCliente,receita=precoCliente*quantidadeProduto,
         lucro= ((precoCliente - preco)*quantidadeProduto),rentabilidade=rentabilidade)
        return itemPedido


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nomeProduto = models.CharField(max_length=100)
    preco = models.BigIntegerField(default=0)
    precoCliente = models.BigIntegerField()
    quantidadeProduto = models.BigIntegerField(default=1)
    receita = models.BigIntegerField()
    multiplo = models.BigIntegerField()
    lucro = models.BigIntegerField()
    rentabilidade = models.CharField(max_length=50,
     choices = [(tag, tag.value) for tag in TipoRentabilidade])

    objects = ItemPedidoManager()
    def __str__(self):
        return (self.produto.nome)

    def getRentabilidade(self):
        return self.rentabilidade

    def getPrecoCliente(self):
        return self.precoCliente
