import factory

from core.product.models import Categoria, Marca, Produto


class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria
    
    nome = factory.Sequence(lambda n: f"Categoria_{n}")

class MarcaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Marca
    
    nome = factory.Sequence(lambda n: f"Marca_{n}")

class ProdutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Produto
    
    nome = "test_produto"
    descricao = "test_descrição"
    marca = factory.SubFactory(MarcaFactory)
    categoria = factory.SubFactory(CategoriaFactory)
    is_active = True
