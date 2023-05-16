from django.contrib import admin
from django.urls import path,include
from caixa import views as vw
from . import views
from hotel.views import nova_reserva
from django.views.generic import TemplateView


urlpatterns = [
        path('novareserva/', nova_reserva, name='reserva'), 
        path('novareservaday/', views.reservaday, name='reservaday'),
        path('lista_reservas/', views.reserva_list, name='lista_reserva'),
        path('lista_reservasday/', views.reservaday_list, name='lista_reservaday'),
        path('procurar_reserva/', views.proc_reserva, name='proc_reserva'),
        path('outra_view/', include('caixa.urls', namespace='parametro')),
    ]
