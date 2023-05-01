from django import forms
from .models import Reserva

class Reservaform(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['pet']
        #widgets = {
            #'data': forms.HiddenInput(),
        #}