from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'ficha'
urlpatterns = [
    path('novopet/', views.ficha, name='ficha')
]
