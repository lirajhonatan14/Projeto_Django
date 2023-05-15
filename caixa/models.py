from django.db import models
from hotel.models import Reserva
from django.contrib.auth.models import User
from ficha.models import FichaDog

class Caixa(models.Model):
    num_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE,null=True, blank=True)
    usuario  = models.CharField(max_length=100)
    pet = models.ForeignKey(FichaDog, on_delete=models.CASCADE)
    relatorio_estadia = models.TextField(max_length=500)
    desconto = models.DecimalField(max_digits=3, decimal_places=1)
    


    class Meta:
            db_table = 'Caixa'
            
            

