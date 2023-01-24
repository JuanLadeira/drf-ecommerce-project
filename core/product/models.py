from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Categoria(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    nome = models.CharField(max_length=80, unique=True)

    class MPPTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.nome

class Produto(models.Model):
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    nome = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    tipo = models.CharField(max_length=10, blank=True, null=True)
    categoria = TreeForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nome
