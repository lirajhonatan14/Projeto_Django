from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from hotel.models import Reserva
import datetime
from django.shortcuts import render, get_object_or_404
from .models import Reserva

def caixa(request, num_reserva):
    reserva_id = request.GET.get('num_reserva')
    reserva = Reserva.objects.get(pk=num_reserva)
    nome = reserva.pet.nome
    usuario = request.user.username
    reserva1 = ServicosAdicionais.objects.get(pk=reserva_id)
    nome_servico = reserva1.nome_servico
    valor_servico = reserva1.valor_servico

    if request.method == 'POST':
        # lógica de fechamento de reserva aqui
        # ...
        reserva.pago = True
        context = {
        'reserva': reserva,
        }
        return render(request, 'caixa.html', {'reserva': reserva, 'animal': nome, 'usuario': usuario,'reserva1': reserva1, 'nome': nome_servico, 'valor': valor_servico})
    else:
        context = {'reserva': reserva, 'nome': nome, 'usuario': usuario,'reserva1': reserva1, 'nome': nome_servico, 'valor': valor_servico}
        return render(request, 'caixa.html', context)
    
def servicos_adicionais(request, num_reserva):
    reserva_id = request.GET.get('num_reserva')
    reserva1 = ServicosAdicionais.objects.get(pk=num_reserva)
    nome_servico = reserva1.nome_servico
    valor_servico = reserva1.valor_servico
    if request.method == 'POST':
        context = {'reserva1': reserva1, 'nome': nome_servico, 'valor': valor_servico}
        return render(request, 'caixa.html', context)

