from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('novareserva/', views.reserva, name='reserva'),
    path('novareserva/', views.reservaday, name='reservaday'),
]
