from django.db import models
from django.db.models.fields.related import ManyToManyField


# Create your models here.
class Certifications(models.Model):
    name = models.CharField('Nome da Certificação', max_length=200)

    def __str__(self):
        return '%s'



class Seller(models.Model):
    name = models.CharField('Nome Completo', max_length=200)
    fantasy_name = models.CharField('Nome Fantasia', max_length=200)
    cep_production = models.CharField('Cep endereço de produção', max_length=9)
    cep_comerce = models.CharField('Cep endereço de comercio', max_length=9)
    address_number_production = models.PositiveIntegerField('Número endereço de produção')
    address_number_comerce = models.PositiveIntegerField('Número endereço de comercio')
    collective_or_individual = models.BooleanField('Produção coletiva ou individual')
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14)
    have_certification = models.BooleanField('Certificação')
    certifications = models.ManyToManyField(Certifications)
    ecological = models.BooleanField('Produção Ecologica')
    ecological_certification = models.BooleanField('Certificação Ecologica')
    organic = models.BooleanField('Organico')
    payment = models.TextField('Métodos de pagamento')
    indigenous_recognizing = models.BooleanField('Reconhecimento indigena')
    quilombola_recognizing = models.BooleanField('Reconhecimento Quilombola')
    state = models.CharField('Estado', max_length=20)
    region = models.CharField('Região', max_length=50)
    singup_date = models.DateTimeField()
    items_sold = models.CharField(max_length=1000)

class Seller_Contact(models.Model):
    telephone = models.PositiveIntegerField('Telefone')
    email = models.CharField('E-mail', max_length=200)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)

class Buyer(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=9)
    house_num = models.PositiveIntegerField()
    singup_date = models.DateTimeField()


class Buyer_Contact(models.Model):
    telephone = models.PositiveIntegerField('Telefone')
    email = models.CharField('E-mail', max_length=200)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)