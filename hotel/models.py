from django.core.exceptions import ValidationError
from django.db import models
from ficha.models import FichaDog
from django.contrib.auth.models import User



class Reserva(models.Model):
    pet = models.ForeignKey(FichaDog, on_delete=models.CASCADE)
    num_reserva = models.IntegerField(primary_key=True, editable=False)
    data_entrada = models.DateField()
    data_saida = models.DateField()
    hora_entrada = models.TimeField()
    usuario  = models.ForeignKey(User, on_delete=models.CASCADE)
    HORARIO_CHOICES = (('2x_dia', 'Duas vezes por dia'),('3x_dia', 'Três vezes por dia'),('personalizado', 'Horário personalizado'),)
    horario_alimentacao = models.CharField(max_length=20, choices=HORARIO_CHOICES)
    horario_personalizado = models.CharField(max_length=20, blank=True, null=True)
    instrucoes_medicamentos = models.CharField(max_length=100, blank=True, null=True)
    ACEITAR_CHOICES = (('Sim', 'Duas vezes por dia'),('3x_dia', 'Três vezes por dia'),('personalizado', 'Horário personalizado'),)
    autorizacao_para_cuidados_medicos = models.BooleanField(default=False, choices=[(False, 'Não'), (True, 'Sim')])
    servicos_adicionais = models.ForeignKey('hotel.ServicosAdicionais', blank=True, on_delete=models.CASCADE)
    
    def clean(self):
        super().clean()
        if self.horario_alimentacao == 'personalizado':
            # Validar o input do usuário para horário personalizado
            # Certifique-se de que o campo "horario_personalizado" seja preenchido
            if not self.horario_personalizado:
                raise ValidationError("Horário personalizado requerido.")
            
    class Meta:
            db_table = 'Reserva_Hotel'
            
    def __str__(self):
        return str(self.num_reserva)

            
class ReservaDay(models.Model):
    #pet = models.ForeignKey(FichaDog, on_delete=models.CASCADE)
    data_entrada = models.DateField()
    data_saida = models.DateField()
    hora_entrada = models.TimeField()
    num_reserva = models.IntegerField(primary_key=True, editable=False)
    usuario  = models.ForeignKey(User, on_delete=models.CASCADE)
    HORARIO_CHOICES = (('2x_dia', 'Duas vezes por dia'),('3x_dia', 'Três vezes por dia'),('personalizado', 'Horário personalizado'),)
    horario_alimentacao = models.CharField(max_length=20, choices=HORARIO_CHOICES)
    horario_personalizado = models.CharField(max_length=20, blank=True, null=True)
    instrucoes_medicamentos = models.CharField(max_length=100, blank=True, null=True)
    ACEITAR_CHOICES = (('Sim', 'Duas vezes por dia'),('3x_dia', 'Três vezes por dia'),('personalizado', 'Horário personalizado'),)
    servicos_adicionais = models.ManyToManyField('hotel.ReservaServicoAdicional', blank=True, null=True)
    autorizacao_para_cuidados_medicos = models.BooleanField(default=False, choices=[(False, 'Não'), (True, 'Sim')])

    
    def clean(self):
        super().clean()
        if self.horario_alimentacao == 'personalizado':
            # Validar o input do usuário para horário personalizado
            # Certifique-se de que o campo "horario_personalizado" seja preenchido
            if not self.horario_personalizado:
                raise ValidationError("Horário personalizado requerido.")
            
    class Meta:
            db_table = 'Reserva_Day'
            
    def __str__(self):
        return str(self.num_reserva)
    
class ServicosAdicionais(models.Model):
    nome_servico = models.CharField(max_length=50, primary_key=True)
    valor_servico = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
            db_table = 'Servicos_adicionais'
            
class ReservaServicoAdicional(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    servico_adicional = models.ForeignKey(ServicosAdicionais, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    class Meta:
            db_table = 'Reserva_Servicos_adicionais'

 
            
        