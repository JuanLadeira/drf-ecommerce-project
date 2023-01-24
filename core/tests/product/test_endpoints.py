import json

import pytest

pytestmark = pytest.mark.django_db 

class TestCategoriaEndpoint():
    endpoint = '/api/categoria/'

    def test_categoria_get(self, categoria_factory, api_client):
        categoria_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
    
    def test_length_categoria(self, api_client):
        response = api_client().get(self.endpoint)
        assert len(json.loads(response.content)) == 4
        


class TestMarcaEndpoint():
    endpoint = '/api/marca/'

    def test_marca_get(self, marca_factory, api_client):
        marca_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200

    def test_length_marca(self, api_client):
        response = api_client().get(self.endpoint)
        assert len(json.loads(response.content)) == 4



class TestProdutoEndpoint():
    endpoint = '/api/produto/'

    def test_produto_get(self, produto_factory, api_client):
        produto_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
    
    def test_length_produto(self, api_client):
        response = api_client().get(self.endpoint)
        assert len(json.loads(response.content)) == 4