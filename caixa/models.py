from django.db import models
from hotel.models import Reserva
from django.contrib.auth.models import User
from ficha.models import FichaDog

class Caixa(models.Model):
    num_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE,null=True, blank=True)
    usuario  = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(FichaDog, on_delete=models.CASCADE)
    relatorio_estadia = models.TextField(max_length=500)
    desconto = models.DecimalField(max_digits=3, decimal_places=2)
    


    class Meta:
            db_table = 'Caixa'
            