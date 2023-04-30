from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DogForm

def ficha(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso')
    else:
        form = DogForm()
    return render(request, 'ficha.html', {'form': form})

