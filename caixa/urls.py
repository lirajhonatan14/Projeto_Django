from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'caixa'
urlpatterns = [
    path('caixa/<int:num_reserva>/', views.caixa_hotel, name='caixa'),  
    path('caixaday/<int:num_reserva>/', views.caixa_day, name='caixaday'),  
    
    path('relatorio/<int:num_reserva>/', views.relatorio_reservas, name='relatorio'),  
    path('relatorioday/<int:num_reserva>/', views.relatorio_reservasday, name='relatorioday'),  
    
      
]
