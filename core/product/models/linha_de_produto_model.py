from django.db import models
from mptt.models import TreeForeignKey
from core.product.models.produto_model import Produto

# Create your models here.

class LinhaDeProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, help_text="Produto", related_name="linhas_de_produto")
    preço = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço do produto")
    sku = models.CharField(max_length=80, help_text="Código do produto")
    estoque = models.IntegerField(help_text="Quantidade em estoque")
    is_active = models.BooleanField(default=False , help_text="Linha de produto ativa") 
    



    def __str__(self):
        return self.sku
