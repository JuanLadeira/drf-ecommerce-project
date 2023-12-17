from django.contrib import admin

from core.product.models.tipo_de_produto_model import TipoDeProduto
from core.product.models.atributo_model import Atributo


class AtributoInline(admin.TabularInline):
    model = Atributo.tipo_de_produto_atributos.through
    

@admin.register(TipoDeProduto)
class TipoDeProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id", "nome")
    list_per_page = 10
    inlines = [AtributoInline]

# Register your models here.

