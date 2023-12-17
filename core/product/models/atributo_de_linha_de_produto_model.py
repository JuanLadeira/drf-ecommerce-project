from django.db import models
from core.product.models.atributo_valor_model import AtributoValor
from core.product.validators.linha_de_produto_validators import validate_atributos_duplicados
# Create your models here.


class AtributoLinhaDeProduto(models.Model):
    linha_de_produto = models.ForeignKey("LinhaDeProduto", on_delete=models.CASCADE, related_name="atributo_linha_de_produto", help_text="Linha de produto")
    atributo_valor = models.ForeignKey(AtributoValor, on_delete=models.CASCADE, related_name="atributo_linha_de_produto_valor", help_text="Valor do atributo")


    class Meta:
        verbose_name = "Atributo de linha de produto"
        verbose_name_plural = "Atributos de linha de produto"
        unique_together = ["linha_de_produto", "atributo_valor"]


    def clean(self) -> None:
        validate_atributos_duplicados(self)
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)