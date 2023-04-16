from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
# Create your views here.



def index(request):
    fotos = Fotografia.objects.order_by("data").filter(publico=True)
    return render(request,'galeria/index.html',{"cards":fotos})

def imagem(request,id):
    foto = get_object_or_404(Fotografia,pk=id)
    return render(request,'galeria/imagem.html',{"foto":foto})

def busca(request):

    fotos = Fotografia.objects.order_by("data").filter(publico=True)

    if "busca" in request.GET:
        buscado = request.GET['busca']
        if buscado:
            fotos = fotos.filter(nome__icontains=buscado)

    return render(request,"galeria/busca.html",{"cards":fotos})