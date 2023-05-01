from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Reservaform

def reserva(request):
    if request.method == 'POST':
        form = Reservaform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso')
    else:
        form = Reservaform()
    return render(request, 'reserva.html', {'form': form})

