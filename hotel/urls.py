from django.contrib import admin
from django.urls import path,include
from . import views
from caixa import views as vw

urlpatterns = [
    path('novareserva/', views.reserva, name='reserva'),
    path('novareservaday/', views.reservaday, name='reservaday'),
    path('lista_reservas/', views.reserva_list, name='lista_reserva'),
    path('outra_view/', include('caixa.urls', namespace='parametro')),
]
