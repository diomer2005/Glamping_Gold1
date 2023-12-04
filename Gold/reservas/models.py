from django.db import models


class Reserva(models.Model):   
    fecha = models.DateField()
    total = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    status = models.BooleanField(default=True)
   
    
def __str__(self):
    return self.fecha


# Create your models here.
