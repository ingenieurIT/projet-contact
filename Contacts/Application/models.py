from msilib.schema import Class
from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    numero = models.CharField(blank=True, max_length=200)
    mail = models.EmailField(max_length=300)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom
    
    
class Numero(models.Model):
    numero =  models.IntegerField()
    
    def __str__(self):
        return self.numero