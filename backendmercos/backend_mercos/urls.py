from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend_mercos import views

urlpatterns = [
    path('usuario/', views.UsuarioGetAll.as_view()),
    path('usuario/<int:pk>/', views.UsuarioDetail.as_view()),
    path('pedido/', views.Pedido.as_view()),
    path('pedido/<int:pk>/', views.PedidoById.as_view()),
    path('produto/', views.Produto.as_view()),
    path('produto/<int:pk>', views.ProdutoById.as_view()),
    path('cliente/', views.Cliente.as_view()),
    path('cliente/<int:pk>', views.ClienteById.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
