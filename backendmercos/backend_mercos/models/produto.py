from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    compra_minima = models.IntegerField(default = 0)
    preco = models.BigIntegerField()

    def __str__(self):
        return self.nome
        
