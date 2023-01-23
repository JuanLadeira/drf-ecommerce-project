import factory

from core.product.models import Categoria, Marca, Produto


class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria
    
    nome = "test_categoria"

class MarcaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Marca
    
    nome = "test_marca"

class ProdutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Produto
    
    nome = "test_produto"
    descricao = "test_descrição"
    marca = factory.SubFactory(MarcaFactory)
    categoria = factory.SubFactory(CategoriaFactory)
