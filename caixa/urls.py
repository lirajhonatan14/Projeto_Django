from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'caixa'
urlpatterns = [
    path('caixa/<int:num_reserva>/', views.caixa_hotel, name='caixa'),  
    path('caixaday/<int:num_reserva>/', views.caixa_day, name='caixaday'),  
    #path('procurar_reserva/', views.ficha_reserva, name='ficha_reserva'),  
    path('relatorio/<int:num_reserva>/', views.relatorio_reservas, name='relatorio'),  
    path('exibir_reserva/<int:num_reserva>/', views.exibir_reserva, name='exibir_reserva'),
    path('relatorioday/<int:num_reserva>/', views.relatorio_reservasday, name='relatorioday'),  
    
      
]
