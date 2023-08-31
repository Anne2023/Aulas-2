from django.db import models

# Create your models here.
class product (models.Model): #aqui fica a herança
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()



    