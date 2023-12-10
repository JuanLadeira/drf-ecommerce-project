from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Categoria(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, help_text="Categoria pai")
    nome = models.CharField(max_length=80, unique=True, help_text="Nome da categoria")
    slug = models.SlugField(max_length=80, unique=True, help_text="Slug da categoria")

    class MPPTMeta:
        order_insertion_by = ['nome']

    def __str__(self):
        return self.nome
