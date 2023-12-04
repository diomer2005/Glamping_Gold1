from django.db import models
from clientes.models import Cliente
from cabañas.models import Cabaña

class Reserva(models.Model):   
    fecha = models.DateField()
    total = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    status = models.BooleanField(default=True)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idCabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
   
    

# Create your models here.
