import pytest

pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestAtributoValorModels:
    def test_atributo_valor_output_string(self, atributo_valor_factory):
        obj = atributo_valor_factory()
        assert obj.__str__() == f'{obj.atributo.name} - {obj.att_valor}'
