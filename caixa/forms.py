from django import forms
from .models import Caixa

class CaixaForm(forms.ModelForm):
    class Meta:
        model = Caixa
        fields = ['relatorio_estadia','desconto']
        widgets = {
            #'usuario': forms.HiddenInput(),
            #'num_reserva': forms.HiddenInput(),
            #'pet': forms.HiddenInput(),
        }
    def save(self, commit=True, usuario=None):
        reserva = super().save(commit=False)
        if usuario:
            reserva.usuario = usuario
        if commit:
            reserva.save()
        return reserva
    

