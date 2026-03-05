from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Produto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    preco = models.CharField(max_length=50)
    custo = models.CharField(max_length=50)
    obs = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.codigo} - {self.marca}"