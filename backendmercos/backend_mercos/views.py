# views.py
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from .models.usuario import Usuario
from .renderers.renderer_usuario import UsuarioJSONRenderer
from .serializers.serializer_usuario import UsuarioSerializer, UsuarioListSerializer

'''

class UsuarioListApiView(ListAPIView):
    model = Usuario
    queryset = Usuario.objects.all()
    permissions_classes = (AllowAny, )
    renderer_classes = (UsuarioJSONRenderer, )
    serializer_class = UsuarioListSerializer

class UsuarioRetrieveApiView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (UsuarioJSONRenderer, )
    serializer_class = UsuarioSerializer
    
    def get(self, request, *args, **kwargs):
      usuario = Usuario.objects.get(id = kwargs['usuario_id']) 
      serializer = self.serializer_class(usuario)
      return Response(serializer.data, status = status.HTTP_200_OK)
'''
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer
