from django.db import models
from clientes.models import Cliente
from cabañas.models import Cabaña

class Reserva(models.Model):   
    fecha = models.DateField()
    total = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    status = models.BooleanField(default=True)

    

# Create your models here.
