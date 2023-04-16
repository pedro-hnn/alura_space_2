from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    CATEGORIAS = [
        ("Nebulosa","NEBULOSA"),("Estrela","ESTRELA"),("Galáxia","GALÁXIA"),("Planeta","PLANETA")
    ]

    nome = models.CharField(max_length=150,null=False,blank=False)
    legenda = models.TextField(null=False,blank=False)
    categoria = models.CharField(choices=CATEGORIAS,default="",max_length=50,null=False,blank=False)
    descricao = models.TextField(null=False,blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%D/",blank=True)
    publico = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now,blank=False)

    def __str__(self):
        return self.nome