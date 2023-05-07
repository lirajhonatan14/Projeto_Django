from django import forms
from .models import FichaDog

class DogForm(forms.ModelForm):
    class Meta:
        model = FichaDog
        fields = ['nome', 'raca', 'idade','sexo', 'peso', 'tipo_alimentacao', 'restricoes_alimentares','nome_tutor','contato_tutor','cpf_tutor','endereco','veterinario_cao', 'observacoes']
        widgets = {
            'data': forms.HiddenInput(),
        }