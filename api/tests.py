from django.test import TestCase
from api.models import *
# Create your tests here.

class PessoaTest(TestCase):

    def create_pessoa(self, nome="Junior", cpf='02514256692', email="example@example.com", endereco={'rua':'rua exemplo', 'numero':'00', 'complemento':'exemplo', 'cidade':'11111', 'uf':'PI'}):
        obj_endereco = Endereco.objects.create(rua=endereco['rua'], numero=endereco['numero'], complemento=endereco['complemento'], cidade=endereco['cidade'], uf=endereco['uf'])
        return Pessoa.objects.create(nome=nome,cpf=cpf,email=email, endereco=obj_endereco)

    def create_endereco(self, rua='rua exemplo', numero='00', complemento='exemplo', cidade='11111', uf='PI'):
        return Endereco.objects.create(rua=rua, numero=numero, complemento=complemento, cidade=cidade, uf=uf)

    def test_pessoa_creation(self):
        p = self.create_pessoa()
        self.assertTrue(isinstance(p, Pessoa))
        self.assertEquals(p.__unicode__(),p.nome)

    def test_endereco_creation(self):
        e = self.create_endereco()
        self.assertTrue(isinstance(e,Endereco))
        self.assertEquals(e.__unicode__(), e.rua)