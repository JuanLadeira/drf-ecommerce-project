# Generated by Django 4.1.5 on 2023-01-24 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_produto_tipo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoria",
            name="nome",
            field=models.CharField(max_length=80, unique=True),
        ),
    ]