from django.urls import path
from galeria.views import index, img

urlpatterns = [
    path('', index, name='home'),
    path('img/<int:foto_id>',img, name='imagem'),
]
