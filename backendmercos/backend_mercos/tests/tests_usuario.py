from django.test import TestCase
from django.urls import reverse,include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from ..models.usuario import Usuario
from ..serializers import UsuarioListSerializer, UsuarioSerializer


class UsuarioTestsEmpty(APITestCase):
    
    def test_dadoNenhumUsuarioCadastrado_entaoListaVazia(self):
        """
        Retornar lista vazia de funcionarios
        """

        url = reverse('usuario')
        response = self.client.get(url, format='json')
        #response = self.client.get('api/usuario/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,[])

class UsuarioTests(APITestCase):

    def setUp(self):
        Usuario.objects.create(id = 1,nome='Joao Silva', email='jsilva@example.com',
                               senha='111111')
        Usuario.objects.create(id = 2,nome='Silva Joao', email='sjoao@example.com',
                               senha='222222')
    def test_dadoNenhumUsuario_criarUsuario_usuarioCriado(self):
        usuario1 = Usuario.objects.get(nome='Joao Silva')
        usuario2 = Usuario.objects.get(nome='Silva Joao')

        self.assertEqual(usuario1.nome,'Joao Silva')
        self.assertEqual(usuario2.nome,'Silva Joao')
        self.assertEqual(usuario1.email,'jsilva@example.com')
        self.assertEqual(usuario2.email,'sjoao@example.com')
        self.assertEqual(usuario1.senha,'111111')
        self.assertEqual(usuario2.senha,'222222')

    def test_dadoUsuariosCadastrados_usuariosEncontrados(self):
        url = reverse('usuario')
        response = self.client.get(url, format='json')
        #response = self.client.get('api/usuario/')
        serializer = UsuarioListSerializer(Usuario.objects.all(),many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)

'''
    def test_dadoBuscarUsuarioPorId_usuarioEncontrado(self):
        url = reverse('usuario_by_id', kwargs ={'pk':4})
        response = self.client.get(url)
        serializer = UsuarioSerializer(Usuario.objects.get(id=1))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)
'''
