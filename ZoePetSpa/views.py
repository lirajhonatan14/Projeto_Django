from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request,'home.html')
