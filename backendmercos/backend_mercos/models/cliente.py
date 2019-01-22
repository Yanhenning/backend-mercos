from django.db import models
from .pedido import Pedido

class Cliente(models.Model):
    pedidos = models.ManyToManyField(Pedido)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
