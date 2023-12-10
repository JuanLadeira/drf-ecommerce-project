import factory

from core.product.models.categoria_model import Categoria

class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria
    
    nome = factory.Sequence(lambda n: f"Categoria_{n}")
    slug = factory.Sequence(lambda n: f"slug_{n}")