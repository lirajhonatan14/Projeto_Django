from django import forms
from .models import ReservaDay, Reserva

class Reservaform(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['pet','data_entrada','data_saida','hora_entrada','horario_alimentacao', 'horario_personalizado','instrucoes_medicamentos','servicos_adicionais', 'autorizacao_para_cuidados_medicos']
        widgets = {
            'usuario': forms.HiddenInput(),
            'num_reserva': forms.HiddenInput(),
        }
    def save(self, commit=True, usuario=None):
        reserva = super().save(commit=False)
        if usuario:
            reserva.usuario = usuario
        if commit:
            reserva.save()
        return reserva
    
class ReservaDayForm(forms.ModelForm):
    class Meta:
        model = ReservaDay
        fields = ['dog','data_entrada','data_saida','hora_entrada','horario_alimentacao', 'horario_personalizado','instrucoes_medicamentos','servicos_adicionais', 'autorizacao_para_cuidados_medicos']
        widgets = {
            'usuario': forms.HiddenInput(),
        }
    def save(self, commit=True, usuario=None):
        reserva1 = super().save(commit=False)
        if usuario:
            reserva1.usuario = usuario
        if commit:
            reserva1.save()
        return reserva1
    