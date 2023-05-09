from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from caixa.forms import CaixaForm
from caixa.models import Caixa
from hotel.models import Reserva




def outra_view_do_outro_app(request):
    meu_dado = request.GET.get('parametro')
    # Fazer algo com o valor do dado
    return HttpResponse('O valor do dado é: ' + meu_dado)

from django.shortcuts import render, get_object_or_404
from .models import Reserva

def caixa(request, num_reserva):
    reserva_id = request.GET.get('num_reserva')
    reserva = Reserva.objects.get(pk=num_reserva)
    nome = reserva.pet.nome
    usuario = request.user.username

    if request.method == 'POST':
        # lógica de fechamento de reserva aqui
        # ...
        return render(request, 'caixa.html', {'reserva': reserva, 'animal': nome, 'usuario': usuario})
    else:
        context = {'reserva': reserva, 'animal': nome, 'usuario': usuario}
        return render(request, 'caixa.html', context)

