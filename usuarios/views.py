from django.shortcuts import render
from usuarios.forms import LoginForms

def login(request):
    forms = LoginForms()
    return render(request, 'usuarios/login.html', {
        'forms':forms
    })

def registrar(request):
    return render(request, 'usuarios/registrar.html')