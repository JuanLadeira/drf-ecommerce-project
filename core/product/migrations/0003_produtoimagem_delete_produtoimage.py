# Generated by Django 4.2.7 on 2023-12-16 18:06

import core.product.fields.order_field
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_rename_preço_linhadeproduto_preco"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProdutoImagem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        blank=True, help_text="Nome da imagem", max_length=255
                    ),
                ),
                (
                    "alternative_text",
                    models.CharField(
                        blank=True,
                        help_text="Texto alternativo da imagem",
                        max_length=255,
                    ),
                ),
                (
                    "url",
                    models.ImageField(help_text="Imagem do produto", upload_to=None),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, help_text="Imagem ativa"),
                ),
                (
                    "ordem",
                    core.product.fields.order_field.OrderField(
                        blank=True, help_text="Ordem das imagens exibidas"
                    ),
                ),
                (
                    "linha_de_produto",
                    models.ForeignKey(
                        help_text="Linha de produto do produto",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="produto_imagem",
                        to="product.linhadeproduto",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ProdutoImage",
        ),
    ]