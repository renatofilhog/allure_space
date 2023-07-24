from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    dados = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    return render(request, "galeria/index.html", {'dados':dados})

def img(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {'foto':foto})