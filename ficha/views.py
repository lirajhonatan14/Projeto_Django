from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DogForm
from django.contrib import messages
from ficha.models import FichaDog
from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login/")
def ficha(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salvo com sucesso')
            return redirect('reserva')

    else:
        form = DogForm()
    return render(request, 'ficha.html', {'form': form})


@login_required(login_url="/auth/login/")
def lista_fichas_cachorros(request):
    cachorros = FichaDog.objects.all()
    return render(request, 'lista_pet.html', {'cachorros': cachorros})

