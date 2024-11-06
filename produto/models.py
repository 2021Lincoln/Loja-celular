from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Produto(models.Model):

    marca = models.CharField(max_length=100)
    def __str__(self):
        return self.marca

    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.descricao

    preco = models.DecimalField(max_digits=10, decimal_places=2)
    def __int__(self):
        return self.preco

    quantidade = models.IntegerField()
    def __int__(self):
        return self.quantidade