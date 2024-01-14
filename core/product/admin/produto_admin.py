from django.contrib import admin

from core.product.models.produto_model import Produto
from core.product.models.linha_de_produto_model import LinhaDeProduto
from django.urls import reverse
from django.utils.safestring import mark_safe

# Register your models here.
    
class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change", args=[instance.id])
        if instance.id:
            link = mark_safe(f'<a href="{url}">Editar</a>')
            return link
        
class  LinhaDeProdutoInline(EditLinkInline,admin.TabularInline):
    model = LinhaDeProduto
    readonly_fields = ("edit",)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 10
    inlines = [LinhaDeProdutoInline]
    
