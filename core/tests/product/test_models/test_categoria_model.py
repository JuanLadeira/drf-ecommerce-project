import pytest
from core.product.models.categoria_model import Categoria
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestCategoriaModels:
    def test_categoria_output_string(self, categoria_factory):
        categoria = categoria_factory()
        assert categoria.__str__() == categoria.nome

    def test_nome_tamanho_maximo(self, categoria_factory):
        categoria = categoria_factory(nome='a'*81)
        with pytest.raises(ValidationError):
            categoria.full_clean()

    def test_name_unico(self, categoria_factory):
        categoria = categoria_factory()
        with pytest.raises(IntegrityError):
            categoria2 = categoria_factory(nome=categoria.nome)

    def test_slug_unico(self, categoria_factory):
        categoria = categoria_factory()
        with pytest.raises(IntegrityError):
            categoria2 = categoria_factory(slug=categoria.slug)

    def test_categoria_ativa(self, categoria_factory):
        categoria = categoria_factory()
        assert categoria.is_active is False


    def test_parent_categoria_on_delete_protect(self, categoria_factory):
        categoria = categoria_factory()
        categoria2 = categoria_factory(parent=categoria)
        with pytest.raises(IntegrityError):
            categoria.delete()


    def test_return_categorias_ativas(self, categoria_factory):
        categoria = categoria_factory()
        categoria2 = categoria_factory(is_active=True)
        qs = Categoria.objects.is_active()

        assert qs.count() == 1

    def test_return_todas_ascategorias_ativas(self, categoria_factory):
        categoria = categoria_factory()
        categoria2 = categoria_factory(is_active=True)
        qs = Categoria.objects.all()

        assert qs.count() == 2