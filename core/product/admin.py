from django.contrib import admin

from .models import Categoria, Marca, Produto, ProdutoLine

# Register your models here.

class ProductLineInline(admin.TabularInline):
    model = ProdutoLine

@admin.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]

admin.site.register(Categoria)

admin.site.register(Marca)
admin.site.register(ProdutoLine)