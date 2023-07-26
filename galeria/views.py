from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia

def index(request):
    dados = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    return render(request, "galeria/index.html", {'dados':dados})

def img(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {'foto':foto})

def buscar(request):
    dados = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    if "termo" in request.GET:
        termo = request.GET['termo']
        if termo:
            dados = dados.filter(nome__icontains=termo)
    else:
        dados = {}

    return render(request, 'galeria/buscar.html', {'dados': dados})
