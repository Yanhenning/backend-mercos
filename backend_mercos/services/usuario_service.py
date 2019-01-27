from ..models.usuario import Usuario as UsuarioModel
from django.http import Http404
from rest_framework import status

def getById(id):
    try:
        return UsuarioModel.objects.get(id=id)
    except UsuarioModel.DoesNotExist:
        raise Http404

def getAll():
    return UsuarioModel.objects.all()
