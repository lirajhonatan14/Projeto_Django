from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from caixa.forms import CaixaForm
from caixa.models import Caixa
from ficha.models import FichaDog




def outra_view_do_outro_app(request):
    meu_dado = request.GET.get('parametro')
    # Fazer algo com o valor do dado
    return HttpResponse('O valor do dado é: ' + meu_dado)

from django.shortcuts import render, get_object_or_404
from .models import Reserva

def caixa(request):
    if request.method == 'POST':
        num_reserva = request.POST.get('num_reserva')
        reserva = get_object_or_404(Reserva, num_reserva=num_reserva)
        nome = reserva.ficha
        usuario = request.user
        total = reserva.total
        if reserva.desconto:
            total = total - reserva.desconto

        if reserva.status == 'Aguardando Pagamento':
            reserva.status = 'Finalizado'
            reserva.save()

        relatorio = Relatorio.objects.create(
            reserva=reserva,
            usuario=usuario,
            data_saida=date.today(),
            observacoes=request.POST.get('observacoes')
        )

        context = {
            'reserva': reserva,
            'animal': animal,
            'usuario': usuario,
            'total': total,
            'relatorio': relatorio,
        }
        return render(request, 'caixa.html', context)
    else:
        return HttpResponseBadRequest('Método inválido')
