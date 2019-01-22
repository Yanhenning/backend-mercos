from rest_framework import serializers
from .models.usuario import Usuario

class UsuarioListSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=200, required = True)
    email = serializers.CharField(max_length=50, required=True)
    
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email')

class UsuarioSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=200, required = True)
    email = serializers.CharField(max_length=50, required=True)
    senha = serializers.CharField(max_length=20, required=True)
    quantidade_pedidos = serializers.CharField(max_length=300,required=False)
    
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'senha', 'quantidade_pedidos')
