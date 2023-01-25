from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Categoria(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    nome = models.CharField(max_length=80, unique=True)

    class MPTTMeta:
        order_insertion_by = ['nome']

    def __str__(self):
        return self.nome

class Produto(models.Model):
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE, related_name='marca')
    slug = models.SlugField(max_length=255)
    nome = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    tipo = models.CharField(max_length=10, blank=True, null=True)
    categoria = TreeForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nome

class ProdutoLine(models.Model):
    product = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="product_line")
    price = models.DecimalField(decimal_places=2, max_digits=4)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    is_active = models.BooleanField(default=False)

