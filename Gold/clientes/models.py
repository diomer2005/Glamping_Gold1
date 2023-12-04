from django.db import models

class Cliente (models.Model):

    nombre = models.CharField(max_length=255)
    documento = models.CharField(max_length=20, unique=True)
    nacionalidad = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    

def __str__(self):
    return self.nombre

# Create your models here.
