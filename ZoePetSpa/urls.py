from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', include('ficha.urls')),
    path('', include('hotel.urls')),
    path('', include('caixa.urls')),
    
    
]
