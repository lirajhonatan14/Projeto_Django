from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseServerError
from django.contrib import messages
from hotel.models import Reserva, ServicosAdicionais
from hotel.forms import ServicosAdicionaisForm
from django.shortcuts import render, get_object_or_404
from .models import Caixa
from .forms import CaixaForm
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime, date
import traceback
from ficha.models import FichaDog
from django.urls import reverse


@login_required(login_url="/auth/login/")
def caixa(request, num_reserva):
    reserva = Reserva.objects.get(num_reserva=num_reserva)
    usuario = request.user.username
    
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
    return render(request, 'caixa.html', context)

    
        
    

from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io

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
    total = calcular_total(reserva)

        # Create a dictionary to hold the data for the PDF
    context = {
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

from datetime import timedelta

def calcular_total(num_reserva, ):
    caixa = Caixa.objects.filter(num_reserva=num_reserva)
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
