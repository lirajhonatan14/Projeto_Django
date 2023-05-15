from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ReservaDayForm, Reservaform, ServicosAdicionaisForm
from datetime import datetime, date
from .models import Reserva, ServicosAdicionais
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Reserva
from django.views.generic import View

@login_required(login_url="/auth/login/")
def nova_reserva(request):
    if request.method == 'POST':
        form_reserva = Reservaform(request.POST)
        form_servicos = ServicosAdicionaisForm(request.POST)
        reserva = form_reserva.save(commit=False)
        reserva.usuario = request.user
        reserva.save()  # Salva a reserva antes de adicionar os serviços
        if form_reserva.is_valid() and form_servicos.is_valid():
            
            servicos = form_servicos.save(commit=False)
            servicos.num_reserva = reserva.num_reserva
            #servicos_adicionais = ServicosAdicionais(num_reserva_id=reserva.pk)
            #servicos_adicionais.save()
            servicos.save()  # Salva os serviços depois da reserva
            #reserva.servicos_adicionais.add(servicos)
            return redirect('home')
    else:
        form_reserva = Reservaform()
        form_servicos = ServicosAdicionaisForm()
    return render(request, 'reserva.html', {'form_reserva': form_reserva, 'form_servicos': form_servicos})







    
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
    reservas = Reserva.objects.filter(data_saida__gte=hoje)

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







