from django.contrib import admin
from .models import Reserva, ReservaDay,ServicosAdicionais

admin.site.register(Reserva)
admin.site.register(ReservaDay)
admin.site.register(ServicosAdicionais)
