from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=80, help_text="Nome da marca")
    
    def __str__(self):
        return self.nome
