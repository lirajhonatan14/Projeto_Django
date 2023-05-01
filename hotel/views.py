from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import Reservaform, ReservaDayForm

@login_required
def reserva(request):
    if request.method == 'POST':
        form = Reservaform(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            messages.success(request, 'Reserva criada com sucesso!')
            return redirect('reserva.html')

    else:
        form = Reservaform()
    return render(request, 'reserva.html', {'form': form})
@login_required
def reservaday(request):
    if request.method == 'POST':
        form = ReservaDayForm(request.POST)
        if form.is_valid():
            reserva1 = form.save(commit=False)
            reserva1.usuario = request.user
            reserva1.save()
            messages.success(request, 'Reserva criada com sucesso!')
            return redirect('reserva.html')
    else:
        form = ReservaDayForm()
    return render(request, 'reserva.html', {'form': form})





