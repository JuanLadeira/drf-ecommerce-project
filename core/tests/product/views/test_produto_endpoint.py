import json

import pytest

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