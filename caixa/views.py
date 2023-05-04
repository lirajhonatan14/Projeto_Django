from django.shortcuts import render,redirect
from django.contrib import messages
from caixa.forms import CaixaForm

def caixa(request):
    if request.method == 'POST':
        form = CaixaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            messages.success(request, 'Reserva criada com sucesso!')
            return redirect('caixa')
    else:
        form = CaixaForm()
    context = {
        'form': form,
    }
    return render(request, 'caixa.html', {'form': form})