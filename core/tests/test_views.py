from urllib import request
from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
        'nome': 'Ana Paula',
        'email': 'ana@email.com',
        'assunto': 'Um assunto qualquer.',
        'mensagem': 'Uma mensagem qualquer.',   
        }
        
        self.cliente = Client()
        
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 200)
        
    def test_form_invalid(self):
        dados = {
            'nome': 'Ana Paula',
            'email': 'ana@email.com',
        }
        
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)