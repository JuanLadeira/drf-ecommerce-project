import pytest

pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestMarcaModels:
    def test_marca_output_string(self, marca_factory):
        marca = marca_factory()
        assert marca.__str__() == marca.nome
