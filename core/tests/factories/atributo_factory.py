import factory

from core.product.models.atributo_model import Atributo

class AtributoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Atributo
    
    name = factory.Sequence(lambda n: f"Categoria_{n}")
    description = factory.Sequence(lambda n: f"Descrição da categoria {n}")