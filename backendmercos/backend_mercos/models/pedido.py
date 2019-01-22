from django.db import models
from enum import Enum
from .usuario import Usuario
from backend_mercos.enums_merc import TipoRentabilidade

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    quantidadeItem = models.BigIntegerField(default=0)
    valor = models.BigIntegerField(default=0)
    rentabilidade = models.CharField(max_length=50,
    choices = [(tag, tag.value) for tag in TipoRentabilidade])
    
    def getRentabilidade(self):
        return self.rentabilidade

    def getValor(self):
        return self.valor

    def getQuantidadeItens(self):
        return self.quantidade_item
