from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'caixa'
urlpatterns = [
    path('caixa/<int:num_reserva>/', views.caixa, name='caixa'),
    
    
    
]
