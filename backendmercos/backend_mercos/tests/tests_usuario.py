from django.test import TestCase
from django.urls import reverse,include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from ..models.usuario import Usuario


class UsuarioTests(APITestCase):
    
    def test_dadoUsuariosCadastrados_usuariosEncontrados(self):
        """
        Garantir que o usuário foi criado
        """

        url = reverse('usuario')
        response = self.client.get(url, format='json')
        #response = self.client.get('api/usuario/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(response.data,'[]')

    def setUp(self):
        Usuario.objects.create(nome='Joao Silva', email='jsilva@example.com',
                               senha='111111')
        Usuario.objects.create(nome='Silva Joao', email='sjoao@example.com',
                               senha='222222')
    def test_puppy(self):
        usuario1 = Usuario.objects.get(nome='Joao Silva')
        usuario2 = Usuario.objects.get(nome='Silva Joao')

        self.assertEqual(usuario1.nome,'Joao Silva')
        self.assertEqual(usuario2.nome,'Silva Joao')
        self.assertEqual(usuario1.email,'jsilva@example.com')
        self.assertEqual(usuario2.email,'sjoao@example.com')
        self.assertEqual(usuario1.senha,'111111')
        self.assertEqual(usuario2.senha,'222222')
