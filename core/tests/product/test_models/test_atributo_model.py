import pytest

pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestAtributoModels:
    def test_atributo_output_string(self, atributo_factory):
        atributo = atributo_factory()
        assert atributo.__str__() == atributo.name
