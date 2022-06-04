from django.db import models


# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    tel = models.CharField(max_length=30)

class Logement(models.Model):
    adresse = models.CharField(max_length=50)
    ville = models.CharField(max_length=30)
    nb_pieces = models.IntegerField()
    date_dispo = models.DateField()
    prix_mise_vente = models.DecimalField(max_digits=15, decimal_places=2)
    superficie = models.DecimalField(max_digits=7, decimal_places=2)
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE,related_name="logements")

    class Type(models.IntegerChoices):
        Appartement = 0
        Maison = 1
        Local = 2

    type = models.IntegerField(choices=Type.choices)

    class Etat(models.IntegerChoices):
        Neuf = 0
        TB_Etat = 1
        B_Etat = 2
        Mauvais_Etat = 3

    type = models.IntegerField(choices=Etat.choices)

class Visite(models.Model):
    date_visite = models.DateField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=False)
    logement = models.ForeignKey(Logement,on_delete=models.CASCADE,null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['client','logement','date'], name='visite_Unique')
        ]

class Vente(models.Model):
    logement = models.ForeignKey(Logement,on_delete=models.CASCADE,null=False,primary_key=True)
    prix_vente = models.DecimalField(max_digits=15, decimal_places=2)
    taux_commission = models.DecimalField(max_digits=5, decimal_places=2)
    client_acheteur = models.ForeignKey(Client,on_delete=models.CASCADE,null=False)
