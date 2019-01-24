from ..models.cliente import Cliente as ClienteModel
from django.http import Http404
from rest_framework import status

def getById(id):
    try:
        return ClienteModel.objects.get(id=id)
    except ClienteModel.DoesNotExist:
        raise Http404

def getAll():
    return ClienteModel.objects.all()
