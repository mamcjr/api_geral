from django.db import models
from .util import estados

# Create your models here.
class Pessoa(models.Model):
    """
    Model para controle de pessoas com dados pessoais
    """

    class Meta:
        db_table = 'pessoa'

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    foto = models.FileField(blank=True, null=True)

    def __unicode__(self):
        return self.nome

class Endereco(models.Model):
    """
    Model para Controle de Endereços
    """

    class Meta:
        db_table = 'endereco'

    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cidade = models.IntegerField()
    uf = models.CharField(max_length=2,choices=estados.STATE_CHOICES)

    def __unicode__(self):
        return self.rua