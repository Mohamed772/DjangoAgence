from django.db import models


# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    tel = models.CharField(max_length=30)
