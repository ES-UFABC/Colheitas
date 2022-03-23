from django.db import models

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    singup_date = models.DateTimeField()
    items_sold = models.CharField(max_length=1000)

class Buyer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    singup_date = models.DateTimeField()