from django import forms
from .models import ReservaDay, Reserva, ServicosAdicionais

class Reservaform(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['pet','data_entrada','data_saida','hora_entrada','horario_alimentacao', 'horario_personalizado','instrucoes_medicamentos', 'autorizacao_para_cuidados_medicos']
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
        fields = ['pet','data_entrada','data_saida','hora_entrada','horario_alimentacao', 'horario_personalizado','instrucoes_medicamentos', 'autorizacao_para_cuidados_medicos']
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

class ServicosAdicionaisForm(forms.ModelForm):
    class Meta:
        model = ServicosAdicionais
        fields = ['nome_servico', 'valor_servico']

class ReservaForm(forms.ModelForm):
    servicos_adicionais = forms.ModelMultipleChoiceField(queryset=ServicosAdicionais.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = Reserva
        fields = ['pet', 'data_entrada', 'data_saida', 'servicos_adicionais']


    