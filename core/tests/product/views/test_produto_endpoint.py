import json

import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db 


class TestProdutoEndpoint():
    endpoint = '/api/produto/'

    def test_produto_get(self, produto_factory, api_client):
        produto_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
    
    def test_length_produto(self, api_client):
        response = api_client().get(self.endpoint)
        assert len(json.loads(response.content)) == 4

    def test_retorna_unico_produto_pelo_slug(self, produto_factory, api_client):
        produto = produto_factory(slug="produto-teste")
        response = api_client().get(f"{self.endpoint}{produto.slug}/")
        assert response.status_code == 200

    def test_retorna_produtos_pela_categoria(self, produto_factory, categoria_factory , api_client):
        categoria = categoria_factory(nome="categoria-teste")
        produto = produto_factory(slug="produto-teste", categoria=categoria)
        response = api_client().get(f"{self.endpoint}/categoria/{categoria.nome}/all/")
        assert response.status_code == 200


