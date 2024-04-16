from django.db import models
from core.product.models.atributo_model import Atributo
# Create your models here.

class TipoDeProduto(models.Model):
    nome = models.CharField(max_length=80, help_text="Nome do tipo de produto")
    atributo = models.ManyToManyField(Atributo, through="TipoDeProdutoAtributos", related_name="tipo_de_produto_atributos", help_text="Atributo")

    def __str__(self):
        return self.nome

