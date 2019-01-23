from django.test import TestCase
from django.urls import reverse,include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from ..models.usuario import Usuario
from ..models.pedido import Pedido
from ..models.item_pedido import ItemPedido
from ..models.produto import Produto
from ..models.cliente import Cliente
from ..serializers import UsuarioListSerializer, UsuarioSerializer, PedidoDetail, PedidoListSerializer, PedidoDetail
