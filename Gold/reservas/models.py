from django.db import models


class Reserva(models.Model):   
    fecha = models.DateField()
    total = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    status = models.BooleanField(default=True)
   
    

# Create your models here.
