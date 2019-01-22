from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)
    quantidade_pedidos = models.BigIntegerField(default=0)

    def __str__(self):
        return self.nome
