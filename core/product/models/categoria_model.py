from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from core.product.querysets.active_queryset import ActiveQueryset
# Create your models here.


class Categoria(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, help_text="Categoria pai")
    nome = models.CharField(max_length=80, unique=True, help_text="Nome da categoria")
    slug = models.SlugField(max_length=80, unique=True, help_text="Slug da categoria")
    
    is_active = models.BooleanField(default=True, help_text="Categoria ativa")

    objects = ActiveQueryset.as_manager()

    class MPPTMeta:
        order_insertion_by = ['nome']

    def __str__(self):
        return self.nome
