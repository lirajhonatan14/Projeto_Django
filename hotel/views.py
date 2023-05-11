from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ReservaDayForm, Reservaform, ServicosAdicionaisForm
from datetime import datetime, date
from .models import Reserva
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ReservaForm, ServicosAdicionaisForm
from .models import Reserva

@login_required(login_url="/auth/login/")

class NovaReservaView(View):
    form_class = ReservaForm
    
    def get(self, request):
        form = self.form_class()
        servicos_form = ServicosAdicionaisForm()
        return render(request, 'reserva.html', {'form': form, 'servicos_form': servicos_form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        servicos_form = ServicosAdicionaisForm(request.POST)
        if form.is_valid() and servicos_form.is_valid():
            reserva = form.save(commit=False)
            reserva.save()
            servicos = servicos_form.save(commit=False)
            servicos.num_reserva = reserva
            servicos.save()
            return redirect('reservas')
        return render(request, 'reserva.html', {'form': form, 'servicos_form': servicos_form})



    
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







