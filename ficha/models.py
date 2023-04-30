from django.db import models

class FichaDog(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=(('M', 'Macho'), ('F', 'Fêmea')))
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_alimentacao = models.CharField(max_length=100)
    restricoes_alimentares = models.CharField(max_length=100, blank=True, null=True)
    contato_proprietario = models.CharField(max_length=100)
    endereco = models.TextField(max_length=100)
    veterinario_cao = models.CharField(max_length=100,blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    data = models.DateTimeField(max_length=100)
   
    
    class Meta:
            db_table = 'Ficha_Dog'


