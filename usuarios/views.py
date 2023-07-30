from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'usuarios/login.html')

def registrar(request):
    return render(request, 'usuarios/registrar.html')