from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'caixa'
urlpatterns = [
    path('caixa/<int:num_reserva>/', views.caixa, name='caixa'),
    path('outra_view/', views.outra_view_do_outro_app, name='parametro'),
    
    
]
