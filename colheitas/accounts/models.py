from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRStateField

class Product(models.Model):
  product_name = models.CharField(max_length=256)

class User(AbstractUser):
  USER_TYPE_CHOICES = (
    (1, 'seller'),
    (2, 'buyer'),
  )
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
  state = BRStateField(blank=True)
  REQUIRED_FIELDS = ['user_type']

class Seller(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  products = models.ManyToManyField(Product) # TODO create product class later
    
