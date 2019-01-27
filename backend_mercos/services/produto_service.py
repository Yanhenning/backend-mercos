from ..models.produto import Produto as ProdutoModel
from django.http import Http404
from rest_framework import status

def getById(id):
    try:
        return ProdutoModel.objects.get(id=id)
    except ProdutoModel.DoesNotExist:
        raise Http404

def getAll():
    return ProdutoModel.objects.all()
