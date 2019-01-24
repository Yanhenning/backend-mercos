from ..models.produto import Produto as ProdutoModel
from django.http import Http404

def getById(id):
        try:
            return ProdutoModel.objects.get(id=id)
        except ProdutoModel.DoesNotExist:
            raise Http404
