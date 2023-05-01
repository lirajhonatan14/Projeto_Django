from django.db import models
from ficha.models import FichaDog

class Reserva(models.Model):
    pet = models.ForeignKey(FichaDog, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5, decimal_places=2)