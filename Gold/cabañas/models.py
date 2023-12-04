from django.db import models

class Cabaña(models.Model):
    nombre = models.CharField(max_length=25)
    capacidad = models.IntegerField()
    descripcion = models.CharField(max_length=25)
    status = models.BooleanField(default=True)

# Create your models here.
