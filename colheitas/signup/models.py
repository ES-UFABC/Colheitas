from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class Certifications(models.Model):
    name = models.CharField(max_length=200)

class Contact(models.Model):
    telephone = models.PositiveIntegerField()
    email = models.CharField(max_lenght = 200)

class Seller(models.Model):
    name = models.CharField(max_length=200)
    fantasy_name = models.CharField(max_length = 200)
    cep_production = models.CharField(max_length = 9)
    cep_comerce = models.CharField(max_length = 9)
    address_number_production = models.PositiveIntegerField()
    address_number_comerce = models.PositiveIntegerField()
    collective_or_individual = models.BooleanField()
    cpf_cnpj = models.CharField(max_length = 14)
    have_certification = models.BooleanField()
    certifications = models.ManyToManyField(Certifications)
    ecological = models.BooleanField()
    ecological_certification = models.BooleanField()
    organic = moddels.BooleanField()
    payment = models.TextField()
    indigenous_recognizing = models.BooleanField()
    quilombola_recognizing = models.BooleanField()
    email = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    singup_date = models.DateTimeField()
    items_sold = models.CharField(max_length=1000)
    contact = ManyToManyField(Contact) 




class Buyer(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    cpf = models.CharField(max_length = 11)
    cep = models.CharField(max_length = 9)
    house_num = models.PositiveIntegerField();
    singup_date = models.DateTimeField()
    contact = ManyToManyField(Contact) 