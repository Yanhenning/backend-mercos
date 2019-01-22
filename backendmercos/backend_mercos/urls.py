from django.conf.urls import url
from .views import UsuarioListApiView, UsuarioRetrieveApiView
app_name = 'backend_mercos'
urlpatterns = [
    url(r'^usuario/$', UsuarioListApiView.as_view()),
    url(r'^usuario/(?P<usuario_id>\w+)/?$', UsuarioRetrieveApiView.as_view()),
]
