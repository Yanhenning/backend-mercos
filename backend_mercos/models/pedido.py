from django.db import models
from enum import Enum
from .usuario import Usuario
from .cliente import Cliente
from backend_mercos.enums_merc import TipoRentabilidade

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    quantidadeItem = models.BigIntegerField(default=0)
    valor = models.BigIntegerField(default=0)
    rentabilidade = models.CharField(max_length=60,
    choices = [(tag, tag.value) for tag in TipoRentabilidade])
