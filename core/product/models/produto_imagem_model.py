from django.db import models
from core.product.models.item import LinhaDeProduto
from core.product.fields.order_field import OrderField
from django.core.exceptions import ValidationError


class ProdutoImagem(models.Model):
    nome = models.CharField(max_length=255, blank=True, help_text="Nome da imagem")
    linha_de_produto = models.ForeignKey(LinhaDeProduto, on_delete=models.CASCADE, related_name="produto_imagem", help_text="Linha de produto do produto")
    alternative_text = models.CharField(max_length=255, blank=True, help_text="Texto alternativo da imagem")
    url = models.ImageField(upload_to=None, help_text="Imagem do produto")
    is_active = models.BooleanField(default=True, help_text="Imagem ativa")
    ordem = OrderField(unique_for_field="linha_de_produto", blank=True, help_text="Ordem das imagens exibidas")

    def __str__(self):
        return self.ordem
    

    def clean(self) -> None:
        qs = ProdutoImagem.objects.filter(linha_de_produto=self.linha_de_produto)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("A ordem da linha de produto deve ser única")
            

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProdutoImagem, self).save(*args, **kwargs)