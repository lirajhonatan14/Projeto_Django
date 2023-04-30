from django import forms
from .models import FichaDog

class DogForm(forms.ModelForm):
    class Meta:
        model = FichaDog
        fields = ['nome', 'raca', 'idade','sexo', 'peso', 'tipo_alimentacao', 'restricoes_alimentares','contato_proprietario','endereco','veterinario_cao', 'observacoes']
        widgets = {
            'data': forms.HiddenInput(),
        }