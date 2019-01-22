from rest_framework import routers
from .backend_mercos.views.view_usuario import UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
