import factory

from core.product.models.marca_model import Marca


class MarcaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Marca
    
    nome = factory.Sequence(lambda n: f"Marca_{n}")

