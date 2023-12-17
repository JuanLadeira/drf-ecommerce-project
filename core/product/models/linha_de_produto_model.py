from collections.abc import Collection
from django.db import models
from django.core.exceptions import ValidationError
from mptt.models import TreeForeignKey
from core.product.models.produto_model import Produto
from core.product.fields.order_field import OrderField
from core.product.models.atributo_valor_model import AtributoValor
from core.product.models.atributo_de_linha_de_produto_model import AtributoLinhaDeProduto
from core.product.models.tipo_de_produto_model import TipoDeProduto
# Create your models here.

class LinhaDeProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, help_text="Produto", related_name="linhas_de_produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço do produto",)
    sku = models.CharField(max_length=80, help_text="Código do produto")
    estoque = models.IntegerField(help_text="Quantidade em estoque")
    is_active = models.BooleanField(default=False , help_text="Linha de produto ativa")
    order = OrderField(unique_for_field="produto", blank=True, help_text="Ordem da linha de produto")
    atributos  = models.ManyToManyField(AtributoValor, through=AtributoLinhaDeProduto, related_name="atributos_linha_de_produto", help_text="Atributos da linha de produto")
    produto_tipo = models.ForeignKey(TipoDeProduto, on_delete=models.PROTECT, null=True, blank=True, help_text="Tipo de produto")

    def __str__(self):
        return self.sku


    def clean(self) -> None:
        qs = LinhaDeProduto.objects.filter(produto=self.produto)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("A ordem da linha de produto deve ser única")
