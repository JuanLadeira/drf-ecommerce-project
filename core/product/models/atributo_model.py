from django.db import models

# Create your models here.


class Atributo(models.Model):
    name = models.CharField(max_length=80, unique=True, help_text="Nome do atributo")
    description = models.TextField(blank=True, help_text="Descrição do atributo")


    def __str__(self) -> str:
        return self.name