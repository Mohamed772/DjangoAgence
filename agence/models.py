from django.db import models


# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    tel = models.CharField(max_length=30)

    def __str__(self):
        return self.nom + ' ' + self.prenom

class Logement(models.Model):
    adresse = models.CharField(max_length=50)
    ville = models.CharField(max_length=30)
    nb_pieces = models.IntegerField()
    date_dispo = models.DateField()
    prix_mise_vente = models.DecimalField(max_digits=15, decimal_places=2)
    superficie = models.DecimalField(max_digits=7, decimal_places=2)
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE,related_name="logements")

    class Type(models.IntegerChoices):
        Appartement = 0, 'Appartement'
        Maison = 1, 'Maison'
        Local = 2, 'Local'

    type = models.IntegerField(choices=Type.choices)

    class Etat(models.IntegerChoices):
        Neuf = 0, 'Neuf'
        TB_Etat = 1, 'Tres bon etat'
        B_Etat = 2, 'Bon etat'
        Mauvais_Etat = 3, 'Mauvais etat'


    etat = models.IntegerField(choices=Etat.choices)

    def __str__(self):
        return str(self.id)+' : '+str(self.prix_mise_vente) + '€ '+ self.get_type_display()+' '+ self.get_etat_display()+' '+ str(self.superficie) +' '+ str(self.nb_pieces) +'pieces '+self.ville

class Visite(models.Model):
    date_visite = models.DateField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=False)
    logement = models.ForeignKey(Logement,on_delete=models.CASCADE,null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['client','logement','date_visite'], name='visite_Unique')
        ]
    def __str__(self):
        return str(self.logement.id) + ' -> ' + self.client.__str__() + ' : ' + str(self.date_visite)

class Vente(models.Model):
    logement = models.ForeignKey(Logement,on_delete=models.CASCADE,null=False,primary_key=True)
    prix_vente = models.DecimalField(max_digits=15, decimal_places=2)
    taux_commission = models.DecimalField(max_digits=5, decimal_places=2)
    client_acheteur = models.ForeignKey(Client,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return str(self.logement.id) + ' -> ' + self.client_acheteur.__str__() + ' : ' + str(self.prix_vente) + ' ( commision : '+ str(self.taux_commission)+ '% )'