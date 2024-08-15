from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from json import dumps


class TestFront(TestCase):
    def setUp(self):
        self.client = APIClient()
               
    def test_home(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
            
    def test_cad_local_get(self):
        res = self.client.get(reverse('cad_local'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cad_local_post(self):
        res = self.client.post(reverse('cad_local'), data={
            'nome':'B3',
            'bloco':'B',
            'capacidade':'45', 
            'tipo':'Sala'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_sucess_page(self):
        res = self.client.get(reverse('success_page'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_cad_recurso_get(self):
        res = self.client.get(reverse('cadastro-recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_recurso_get(self):
        res = self.client.get(reverse('reserva_recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_recurso_post(self):
        res = self.client.post(reverse('reserva_recurso'), 
            data={
                'descricao':'SEMANA DA INFORMÁTICA',
                'horarios': 'M1',
                'dias':'1',
                'qtd_pessoas':10,
                'bloco':'B',
                'local': 'B1',
                'matSolicitante':'202401'
            }
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_listar_emprestimos_get(self):
        res = self.client.get(reverse('listar_emprestimos'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_listar_local_get(self):
        res = self.client.get(reverse('listar_local'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_listar_recursos_get(self):
        res = self.client.get(reverse('listar-recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)