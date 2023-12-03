import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from core.tests.factories import CategoriaFactory, MarcaFactory, ProdutoFactory, LinhaDeProdutoFactory

register(CategoriaFactory)
register(MarcaFactory)
register(ProdutoFactory)
register(LinhaDeProdutoFactory)

@pytest.fixture
def api_client():
    return APIClient