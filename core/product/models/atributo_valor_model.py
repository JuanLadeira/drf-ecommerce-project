from django.db import models
from core.product.models.atributo_model import Atributo

# Create your models here.


class AtributoValor(models.Model):
    att_valor = models.CharField(max_length=80, unique=True,verbose_name="Valor do atributo" , help_text="Valor do atributo")
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE, related_name="atributo_valor", help_text="Atributo")

    def __str__(self) -> str:
        return f'{self.atributo.name} - {self.att_valor}'
    
    class Meta:
        verbose_name = "Valor do atributo"
        verbose_name_plural = "Valores do atributo"
