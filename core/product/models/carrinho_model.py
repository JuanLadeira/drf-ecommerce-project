from django.db import models
from core.product.models.produto_model import Produto
from core.product.models.linha_de_produto_model import LinhaDeProduto
from django.conf import settings

class CarrinhoItem(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carrinho_items')
    sessao_id = models.CharField(max_length=40, blank=True, null=True)
    item = models.ForeignKey(LinhaDeProduto, on_delete=models.CASCADE, related_name='carrinho_items')
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} de {self.item.sku}"

class Carrinho(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carrinho')
    itens = models.ManyToManyField(CarrinhoItem, related_name='carrinhos')

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"
