from django import forms
from .models import Caixa

class CaixaForm(forms.ModelForm):
    class Meta:
        model = Caixa
        fields = ['num_reserva','pet',]
        widgets = {
            'usuario': forms.HiddenInput(),
            #'num_reserva': forms.HiddenInput(),
        }
    def save(self, commit=True, usuario=None):
        reserva = super().save(commit=False)
        if usuario:
            reserva.usuario = usuario
        if commit:
            reserva.save()
        return reserva