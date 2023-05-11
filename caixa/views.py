from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from hotel.models import Reserva
import datetime
from django.shortcuts import render, get_object_or_404
from .models import Reserva
from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login/")
def caixa(request, num_reserva):
    reserva_id = request.GET.get('num_reserva')
    reserva = Reserva.objects.get(pk=num_reserva)
    nome = reserva.pet.nome
    usuario = request.user.username


    if request.method == 'POST':
        # lógica de fechamento de reserva aqui
        # ...
        reserva.pago = True
        context = {
        'reserva': reserva,
        }
        return render(request, 'caixa.html', {'reserva': reserva, 'animal': nome, 'usuario': usuario})
    else:
        context = {'reserva': reserva, 'nome': nome, 'usuario': usuario}
        return render(request, 'caixa.html', context)
    


