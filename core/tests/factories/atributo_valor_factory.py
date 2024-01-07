import factory

from core.product.models.atributo_valor_model import AtributoValor
from core.tests.factories.atributo_factory import AtributoFactory

class AtributoValorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AtributoValor
    
    att_valor = factory.Sequence(lambda n: f"valor {n}")
    atributo = factory.SubFactory(AtributoFactory)