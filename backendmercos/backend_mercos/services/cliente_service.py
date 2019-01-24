from ..models.cliente import Cliente as ClienteModel
from django.http import Http404

def getById(id):
        try:
            return ClienteModel.objects.get(id=id)
        except ClienteModel.DoesNotExist:
            raise Http404
