from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend_mercos import views

urlpatterns = [
    path('usuario/', views.Usuario.as_view(),name='usuario'),
    path('usuario/<int:pk>/', views.UsuarioDetail.as_view(),name='usuario_by_id'),
    path('pedido/', views.Pedido.as_view(), name='pedido'),
    path('pedido/<int:pk>/', views.PedidoById.as_view(),name='pedido_by_id'),
    path('produto/', views.Produto.as_view(), name='produto'),
    path('produto/<int:pk>', views.ProdutoById.as_view(), name='produto_id'),
    path('cliente/', views.Cliente.as_view(), name='cliente'),
    path('cliente/<int:pk>', views.ClienteById.as_view(), name='cliente_id'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
