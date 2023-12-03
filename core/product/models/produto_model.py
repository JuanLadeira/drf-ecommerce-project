from django.db import models
from mptt.models import TreeForeignKey
from core.product.models.categoria_model import Categoria

# Create your models here.



class Produto(models.Model):
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    nome = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    tipo = models.CharField(max_length=10, blank=True, null=True)
    categoria = TreeForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
