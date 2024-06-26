# Generated by Django 4.2.7 on 2023-12-13 00:37

import core.product.fields.order_field
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                        help_text="Nome da categoria", max_length=80, unique=True
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Slug da categoria", max_length=80, unique=True
                    ),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        help_text="Categoria pai",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.categoria",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="LinhaDeProduto",
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
                    "preço",
                    models.DecimalField(
                        decimal_places=2, help_text="Preço do produto", max_digits=10
                    ),
                ),
                ("sku", models.CharField(help_text="Código do produto", max_length=80)),
                ("estoque", models.IntegerField(help_text="Quantidade em estoque")),
                (
                    "is_active",
                    models.BooleanField(
                        default=False, help_text="Linha de produto ativa"
                    ),
                ),
                (
                    "order",
                    core.product.fields.order_field.OrderField(
                        blank=True, help_text="Ordem da linha de produto"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Marca",
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
                ("nome", models.CharField(help_text="Nome da marca", max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="ProdutoImage",
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
                        related_name="produto_image",
                        to="product.linhadeproduto",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Produto",
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
                    "slug",
                    models.SlugField(
                        help_text="Slug do produto", max_length=80, unique=True
                    ),
                ),
                ("nome", models.CharField(help_text="Nome do produto", max_length=80)),
                (
                    "descricao",
                    models.TextField(blank=True, help_text="Descrição do produto"),
                ),
                (
                    "is_digital",
                    models.BooleanField(default=False, help_text="Produto digital"),
                ),
                (
                    "tipo",
                    models.CharField(
                        blank=True,
                        help_text="Tipo do produto",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, help_text="Produto ativo"),
                ),
                (
                    "categoria",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        help_text="Categoria do produto",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="product.categoria",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        help_text="Marca do produto",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.marca",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="linhadeproduto",
            name="produto",
            field=models.ForeignKey(
                help_text="Produto",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="linhas_de_produto",
                to="product.produto",
            ),
        ),
    ]
