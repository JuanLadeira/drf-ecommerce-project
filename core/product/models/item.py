from collections.abc import Collection
from django.db import models
from django.core.exceptions import ValidationError
from mptt.models import TreeForeignKey
from core.product.models.produto_model import Produto
from core.product.fields.order_field import OrderField

# Create your models here.

class Item(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, help_text="Produto", related_name="linhas_de_produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço do produto",)
    sku = models.CharField(max_length=80, help_text="Código do produto")
    estoque = models.IntegerField(help_text="Quantidade em estoque")
    is_active = models.BooleanField(default=False , help_text="Linha de produto ativa")
    order = OrderField(unique_for_field="produto", blank=True, help_text="Ordem da linha de produto")



    def __str__(self):
        return self.sku


    def clean(self) -> None:
        qs = Item.objects.filter(produto=self.produto)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("A ordem do item deve ser única")
