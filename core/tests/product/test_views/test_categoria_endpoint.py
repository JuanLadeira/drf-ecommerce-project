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