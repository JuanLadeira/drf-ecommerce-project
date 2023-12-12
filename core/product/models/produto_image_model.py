from django.db import models
from core.product.models.linha_de_produto_model import LinhaDeProduto
from core.product.fields.order_field import OrderField
from django.core.exceptions import ValidationError


class ProdutoImage(models.Model):
    nome = models.CharField(max_length=255, blank=True, help_text="Nome da imagem")
    linha_de_produto = models.ForeignKey(LinhaDeProduto, on_delete=models.CASCADE, related_name="produto_image", help_text="Linha de produto do produto")
    alternative_text = models.CharField(max_length=255, blank=True, help_text="Texto alternativo da imagem")
    url = models.ImageField(upload_to=None, help_text="Imagem do produto")
    is_active = models.BooleanField(default=True, help_text="Imagem ativa")
    ordem = OrderField(unique_for_field="linha_de_produto", blank=True, help_text="Ordem das imagens exibidas")

    def __str__(self):
        return self.nome
    

    def clean(self) -> None:
        qs = ProdutoImage.objects.filter(produto=self.linha_de_produto)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("A ordem da linha de produto deve ser única")
            

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProdutoImage, self).save(*args, **kwargs)