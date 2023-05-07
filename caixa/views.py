from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from caixa.forms import CaixaForm
from caixa.models import Caixa
from ficha.models import FichaDog




def outra_view_do_outro_app(request):
    meu_dado = request.GET.get('parametro')
    # Fazer algo com o valor do dado
    return HttpResponse('O valor do dado é: ' + meu_dado)

from django.shortcuts import render, get_object_or_404
from .models import Reserva

def caixa(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    nome_animal = Reserva.pet # recupera o nome do animal
    num_reserva = Reserva.num_reserva # recupera o número da reserva
    usuario = request.user # recupera o usuário logado
    relatorio = Caixa.relatorio_estadia
    desconto = Caixa.desconto
    
    

    # Lógica para fechamento da reserva e pagamento

    return render(request, 'caixa.html', {'nome_animal': nome_animal, 'num_reserva': num_reserva, 'usuario': usuario, 'relatorio': relatorio, 'desconto': desconto})
