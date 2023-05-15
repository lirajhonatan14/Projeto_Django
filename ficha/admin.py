from django.contrib import admin
from .models import FichaDog

@admin.register(FichaDog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['nome']
    #list_filter = ('nome')
    #search_fields = ('nome')
