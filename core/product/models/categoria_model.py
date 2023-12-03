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
