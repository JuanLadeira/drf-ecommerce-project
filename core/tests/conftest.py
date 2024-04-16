import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from core.tests.factories.categoria_factory import CategoriaFactory
from core.tests.factories.marca_factory import MarcaFactory
from core.tests.factories.produto_factory import ProdutoFactory
from core.tests.factories.item_factory import LinhaDeProdutoFactory
from core.tests.factories.produto_imagem_factory import ProdutoImagemFactory

register(ProdutoImagemFactory)
register(CategoriaFactory)
register(MarcaFactory)
register(ProdutoFactory)
register(LinhaDeProdutoFactory)

@pytest.fixture
def api_client():
    return APIClient