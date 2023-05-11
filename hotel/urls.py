from django.contrib import admin
from django.urls import path,include
from caixa import views as vw
from . import views
from .views import NovaReservaView


urlpatterns = [
    path('novareserva/', NovaReservaView, name='nova_reserva'),
    path('novareservaday/', views.reservaday, name='reservaday'),
    path('lista_reservas/', views.reserva_list, name='lista_reserva'),
    path('procurar_reserva/', views.proc_reserva, name='proc_reserva'),
    path('outra_view/', include('caixa.urls', namespace='parametro')),
]
