from django.db import models
from mptt.models import TreeForeignKey
from core.product.models.categoria_model import Categoria
from core.product.models.marca_model import Marca
from core.product.models.tipo_de_produto_model import TipoDeProduto

# Create your models here.



class Produto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, help_text="Marca do produto")
    slug = models.SlugField(max_length=80, unique=True, help_text="Slug do produto")
    nome = models.CharField(max_length=80, help_text="Nome do produto")
    descricao = models.TextField(blank=True, help_text="Descrição do produto")
    is_digital = models.BooleanField(default=False, help_text="Produto digital")
    tipo_produto = models.ForeignKey(TipoDeProduto, on_delete=models.CASCADE, related_name="produto" , help_text="Tipo de produto")
    categoria = TreeForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, help_text="Categoria do produto")
    is_active = models.BooleanField(default=True, help_text="Produto ativo")


    def __str__(self):
        return self.nome

    