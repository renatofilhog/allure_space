from django.urls import path
from galeria.views import index, img

urlpatterns = [
    path('', index, name='home'),
    path('img/',img, name='imagem'),
]
