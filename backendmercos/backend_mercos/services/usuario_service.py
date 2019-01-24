from ..models.usuario import Usuario as UsuarioModel
from django.http import Http404

def getById(id):
        try:
            return UsuarioModel.objects.get(id=id)
        except UsuarioModel.DoesNotExist:
            raise Http404
