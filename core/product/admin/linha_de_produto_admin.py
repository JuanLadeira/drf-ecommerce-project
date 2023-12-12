from django.contrib import admin
from core.product.models.linha_de_produto_model import LinhaDeProduto
from core.product.models.produto_image_model import ProdutoImage




class ProdutoImageInline(admin.TabularInline):
    model = ProdutoImage
    


@admin.register(LinhaDeProduto)
class LinhaDeProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "produto", "categoria")
    list_display_links = ("id", )
    list_per_page = 10
    inlines = [ProdutoImageInline]
    
     
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(produto__isnull=False)
        return qs
    
    def categoria(self, instance):
        return instance.produto.categoria
    
    def produto(self, instance):
        return instance.produto.nome
    
    def marca(self, instance):
        return instance.produto.marca
    
    categoria.short_description = "Categoria"
    produto.short_description = "Produto"
    marca.short_description = "Marca"