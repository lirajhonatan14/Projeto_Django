from django.http import HttpResponse, HttpResponseServerError
from django.contrib import messages
from hotel.models import Reserva, ReservaDay
from django.shortcuts import render, get_object_or_404,redirect
from .models import Caixa, CaixaDay
from .forms import CaixaForm, CaixaDayForm
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from io import BytesIO
from django.urls import reverse
from django.utils import timezone
from django.template.loader import get_template
from xhtml2pdf import pisa
import io
from ficha.models import FichaDog

@login_required(login_url="/auth/login/")
def caixa_hotel(request, num_reserva):
    reserva = Reserva.objects.get(num_reserva=num_reserva)
    usuario = request.user.username
    total_reserva = calcular_total(reserva.num_reserva)
    desc = caixa.desconto
    serv_adicional = reserva.servicos_adicionais.valor_servico
    soma = (desc/100) * total_reserva
    total = (total_reserva - soma) + serv_adicional
    if request.method == 'POST':
        caixa_form = CaixaForm(request.POST)
        if caixa_form.is_valid():
            # Get the cleaned form data
            cleaned_data = caixa_form.cleaned_data
            
            # Get the pet associated with the reservation
            pet = reserva.pet
            
            # Create a new Caixa object using the form data and pet
            caixa = Caixa.objects.create(
                num_reserva=reserva,
                usuario=usuario,
                pet=pet,
                relatorio_estadia=cleaned_data['relatorio_estadia'],
                desconto=cleaned_data['desconto'],
            )
            
            return redirect('caixa:relatorio', num_reserva=num_reserva)
        else:
            # Print out the form data and validation errors
            print(caixa_form.cleaned_data)
            print(caixa_form.errors)
    else:
        caixa_form = CaixaForm()
    
    context = {
        'reserva': reserva,
        'usuario': usuario,
        'caixa_form': caixa_form,
    }
    return render(request, 'caixa.html', context, total)

def caixa_day(request, num_reserva):
    reserva = ReservaDay.objects.get(num_reserva=num_reserva)
    caixaday = CaixaDay.objects.get(num_reserva=reserva)
    usuario = request.user.username
    
    desc = caixaday.desconto
    serv_adicional = reserva.servicos_adicionais.valor_servico
    soma = (desc/100) * 60
    total = (60 - soma) + serv_adicional
    if request.method == 'POST':
        caixa_form = CaixaDayForm(request.POST)
        if caixa_form.is_valid():
            # Get the cleaned form data
            cleaned_data = caixa_form.cleaned_data
            
            # Get the pet associated with the reservation
            pet = reserva.pet
            
            # Create a new Caixa object using the form data and pet
            caixaday = CaixaDay.objects.create(
                num_reserva=reserva,
                usuario=usuario,
                pet=pet,
                relatorio_estadia=cleaned_data['relatorio_estadia'],
                desconto=cleaned_data['desconto'],
            )
            
            return redirect('caixa:relatorioday', num_reserva=num_reserva)
        else:
            # Print out the form data and validation errors
            print(caixa_form.cleaned_data)
            print(caixa_form.errors)
    else:
        caixa_form = CaixaDayForm()
    
    context = {
        'reserva': reserva,
        'usuario': usuario,
        'caixa_form': caixa_form,
    }
    return render(request, 'caixa_day.html', context, total)    
        
    



def relatorio_reservas(request, num_reserva):
    # Get the Caixa objects for the given num_reserva
    caixas = Caixa.objects.filter(num_reserva=num_reserva)
    hora_atual = timezone.now().time()
    
    # Create a list to hold the data for each Caixa object
    context_list = []

    # Loop through the queryset and create a dictionary for each Caixa object
    for caixa in caixas:
        # Get the Reserva and Pet objects associated with the Caixa object
        reserva = caixa.num_reserva
        pet = caixa.pet
    
    total = caixa_hotel(total)
    total_day = caixa_day(total)
        # Create a dictionary to hold the data for the PDF
    context = {
        'total_day':total_day,
        'total': total,
        'hora_atual':hora_atual,
        'reserva': reserva,
        'num_reserva': reserva.num_reserva,
        'nome_pet': pet.nome,
        'nome_tutor': pet.nome_tutor,
        'cpf_tutor': pet.cpf_tutor,
        'data_entrada': reserva.data_entrada,
        'hora_entrada': reserva.hora_entrada,
        'data_saida': reserva.data_saida,
        'usuario': reserva.usuario,
        'relatorio':caixa.relatorio_estadia,
        'desconto':caixa.desconto,

        
    }

    context_list.append(context)

    # Render the PDF template with the context data
    template_path = 'relatorio_reservas.html'
    template = get_template(template_path)
    html = template.render({'context_list': context_list})

    # Create a BytesIO buffer to receive the PDF output
    buffer = io.BytesIO()

    # Generate the PDF output using the BytesIO buffer
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), buffer)

    # Return the PDF as an HTTP response
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'filename="relatorio_reservas.pdf"'
    return response

def relatorio_reservasday(request, num_reserva):
    # Get the Caixa objects for the given num_reserva
    caixas = CaixaDay.objects.filter(num_reserva=num_reserva)
    hora_atual = timezone.now().time()
    
    # Create a list to hold the data for each Caixa object
    context_list = []

    # Loop through the queryset and create a dictionary for each Caixa object
    for caixa in caixas:
        # Get the Reserva and Pet objects associated with the Caixa object
        reserva = caixa.num_reserva
        pet = caixa.pet
    
    total = caixa_hotel(total)
    total_day = caixa_day(total)
        # Create a dictionary to hold the data for the PDF
    context = {
        'total_day':total_day,
        'total': total,
        'hora_atual':hora_atual,
        'reserva': reserva,
        'num_reserva': reserva.num_reserva,
        'nome_pet': pet.nome,
        'nome_tutor': pet.nome_tutor,
        'cpf_tutor': pet.cpf_tutor,
        'data': reserva.data,
        'hora_entrada': reserva.hora_entrada,
        'usuario': reserva.usuario,
        'relatorio':caixa.relatorio_estadia,
        'desconto':caixa.desconto,

        
    }

    context_list.append(context)

    # Render the PDF template with the context data
    template_path = 'relatorio_reservasday.html'
    template = get_template(template_path)
    html = template.render({'context_list': context_list})

    # Create a BytesIO buffer to receive the PDF output
    buffer = io.BytesIO()

    # Generate the PDF output using the BytesIO buffer
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), buffer)

    # Return the PDF as an HTTP response
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'filename="relatorio_reservas.pdf"'
    return response

def calcular_total(num_reserva, ):
    caixa = Caixa.objects.filter(num_reserva=num_reserva).first()
    data_entrada = caixa.num_reserva.data_entrada
    data_saida = caixa.num_reserva.data_saida
    
    peso = caixa.pet.peso
    if peso <= 9:
        porte = "P"
    if peso >= 10 and peso <25:
        porte = "M"
    if peso >= 25:
        porte = "G"    
        
    duracao = (data_saida - data_entrada).days
    
    if duracao <= 4 and porte == "P":
        taxa = 75
    if duracao <= 4 and porte == "M":
        taxa = 85
    if duracao <= 4 and porte == "G":
        taxa = 95
    if duracao > 4 and duracao <= 9 and porte == "P":
        taxa = 70
    if duracao > 4 and duracao <= 9 and porte == "M":
        taxa = 80
    if duracao > 4 and duracao <= 9 and porte == "G":
        taxa = 90  
    if duracao > 9 and duracao <= 14 and porte == "P":
        taxa = 65 
    if duracao > 9 and duracao <= 14 and porte == "M":
        taxa = 75 
    if duracao > 9 and duracao <= 14 and porte == "G":
        taxa = 85 
    if duracao > 15 and duracao <= 19 and porte == "P":
        taxa = 60  
    if duracao > 15 and duracao <= 19 and porte == "M":
        taxa = 70    
    if duracao > 15 and duracao <= 19 and porte == "G":
        taxa = 80 
    if duracao > 19 and porte == "P":
        taxa = 55 
    if duracao > 19 and porte == "M":
        taxa = 65 
    if duracao > 19 and porte == "G":
        taxa = 75 
        
    total = duracao * taxa
    return total

def ficha_reserva(request):
    if request.method == 'POST':
        nome_pet = request.POST.get('pet')
        try:
            reserva = Reserva.objects.get(pet__nome=nome_pet)
            return render(request, 'ficha_reserva.html', {'reserva': reserva})
        except Reserva.DoesNotExist:
            return render(request, 'reserva_nao_encontrada.html')
    return render(request, 'proc_reserva.html')

def exibir_reserva(request, num_reserva):
    reserva = get_object_or_404(Reserva, num_reserva=num_reserva)
    return render(request, 'ficha_reserva.html', {'pet': reserva})
