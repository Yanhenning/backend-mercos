from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend_mercos import views

urlpatterns = [
    path('usuario/', views.Usuario.as_view(),name='usuario'),
    path('usuario/<int:id>/', views.UsuarioById.as_view(),name='usuario_by_id'),
    path('pedido/', views.Pedido.as_view(), name='pedido'),
    path('pedido/<int:id>/', views.PedidoById.as_view(),name='pedido_by_id'),
    path('produto/', views.Produto.as_view(), name='produto'),
    path('produto/<int:id>', views.ProdutoById.as_view(), name='produto_by_id'),
    path('cliente/', views.Cliente.as_view(), name='cliente'),
    path('itempedido/<int:id>',views.ItemPedidoById.as_view(), name='itemPedido_by_id'),
    path('cliente/<int:id>', views.ClienteById.as_view(), name='cliente_by_id'),
    path('usuario/<int:id>/pedido/', views.PedidoByIdUsuario.as_view(), name='pedidos_cliente'),
]
