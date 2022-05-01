from django.db import models
from localflavor.br.models import BRStateField

# Create your models here.      
class Typology(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Tipologia', max_length=200)


class Product(models.Model):
    MEASURE = (
        (1, "Und"), 
        (2, "L"), 
        (3, "g"), 
        (4, "Kg")
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome do Produto', max_length=200)
    price = models.FloatField('Preço', max_length=10)
    measure = models.IntegerField('Unidade de Medida', choices=MEASURE)
    quantity = models.FloatField('Quantidade', max_length=10)
    # typology = models.ForeignKey(Typology, on_delete=models.CASCADE)
    # seller = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    seller = models.ForeignKey("accounts.Seller", on_delete=models.CASCADE)
    state = BRStateField(blank=True)
