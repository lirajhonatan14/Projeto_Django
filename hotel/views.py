from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ReservaDayForm, Reservaform
from datetime import datetime, date
from .models import Reserva

def tela_reserva(request):
    return render(request, 'tela_reserva.html')

@login_required
def reserva(request):
    if request.method == 'POST':
        form = Reservaform(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            messages.success(request, 'Reserva criada com sucesso!')
            return redirect('caixa', num_reserva=reserva.id)
    else:
        form = Reservaform()
    context = {
        'form': form,
    }
    return render(request, 'reserva.html', {'form': form})
@login_required
def reservaday(request):
    if request.method == 'POST':
        form1 = ReservaDayForm(request.POST)
        if form1.is_valid():
            reserva1 = form1.save(commit=False)
            reserva1.usuario = request.user
            reserva1.save()
            messages.success(request, 'Reserva criada com sucesso!')
            return redirect('reserva_day.html')
    else:
        form1 = ReservaDayForm()
    return render(request, 'reserva_day.html', {'form': form1})



def reserva_list(request):
    hoje = date.today()  # obtém a data atual
    reservas = Reserva.objects.filter(data_saida__gte=hoje)

    context = {
        'reservas': reservas
    }
    return render(request, 'lista_reservas.html', context)





