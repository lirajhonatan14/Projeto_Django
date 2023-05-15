from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ReservaDayForm, Reservaform
from datetime import datetime, date
from .models import Reserva, ReservaServicoAdicional
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Reserva
from django.views.generic import View
from django.core.exceptions import ValidationError

@login_required(login_url="/auth/login/")
# views.py
def nova_reserva(request):
    if request.method == 'POST':
        form_reserva = Reservaform(request.POST)
        if form_reserva.is_valid():
            reserva = form_reserva.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            form_reserva.save_m2m()
            servicos_adicionais = form_reserva.cleaned_data['servicos_adicionais']
            #for servico_adicional in servicos_adicionais:
                #ReservaServicoAdicional.objects.create(reserva=reserva, servico_adicional=servico_adicional)
            return redirect('home')
    else:   
        form_reserva = Reservaform()
    return render(request, 'reserva.html', {'form_reserva': form_reserva})






    
@login_required(login_url="/auth/login/")
def reservaday(request):
    if request.method == 'POST':
        form1 = ReservaDayForm(request.POST)
        if form1.is_valid():
            reserva1 = form1.save(commit=False)
            reserva1.usuario = request.user
            reserva1.save()
            messages.success(request, 'Reserva criada com sucesso!')
            return redirect('caixa', num_reserva=reserva1.id)
    else:
        form1 = ReservaDayForm()
    return render(request, 'reserva_day.html', {'form': form1})


@login_required(login_url="/auth/login/")
def reserva_list(request):
    hoje = date.today()  # obtém a data atual
    reservas = Reserva.objects.filter(data_saida__gte=hoje, pago=False)

    context = {
        'reservas': reservas
    }
    return render(request, 'lista_reservas.html', context)


@login_required(login_url="/auth/login/")
def proc_reserva(request):
    hoje = date.today()  # obtém a data atual
    reservas = Reserva.objects.all()

    context = {
        'reservas': reservas
    }
    return render(request, 'procurar_reserva.html', context)







