from django.db import models
from core.product.models.atributo_model import Atributo
# Create your models here.

class TipoDeProduto(models.Model):
    nome = models.CharField(max_length=80, help_text="Nome do tipo de produto")
    atributo = models.ManyToManyField("Atributo", through="TipoDeProdutoAtributos", related_name="tipo_de_produto_atributos", help_text="Atributo")

    def __str__(self):
        return str(self.nome)

# Create your models here.

class TipoDeProdutoAtributos(models.Model):
    """Classe que representa a relação entre Tipo de produto e atributos"""
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE, related_name="tipo_de_produto_atributos_at", help_text="Atributo")
    tipo_de_produto = models.ForeignKey(TipoDeProduto, on_delete=models.CASCADE, related_name="tipo_de_produto_atributos_tp", verbose_name="Tipo de produto", help_text="Tipo de produto")
    

    class Meta:
        unique_together = ['atributo', 'tipo_de_produto']