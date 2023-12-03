from django.contrib import admin

from core.product.models.produto_model import Produto
from core.product.models.linha_de_produto_model import LinhaDeProduto

# Register your models here.

class  LinhaDeProdutoInline(admin.TabularInline):
    model = LinhaDeProduto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "marca", "categoria")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 10
    inlines = [LinhaDeProdutoInline]

