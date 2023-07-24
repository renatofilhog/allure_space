from datetime import datetime

from django.db import models

# Create your models here.

class Fotografia(models.Model):
    OPCOES_CATEGORIAS = [
        ("ESTRELA","Estrela"),
        ("NEBULOSA","Nebulosa"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA", "Planeta")
    ]
    nome = models.CharField(max_length=100,null=False,blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return f'Fotografia: {self.nome} / Legenda: {self.legenda}'