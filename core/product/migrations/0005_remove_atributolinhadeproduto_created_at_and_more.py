# Generated by Django 4.2.7 on 2023-12-17 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_atributo_atributovalor_atributolinhadeproduto_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="atributolinhadeproduto",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="atributolinhadeproduto",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="atributolinhadeproduto",
            name="updated_at",
        ),
    ]