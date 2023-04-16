from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.


class ListaFotos(admin.ModelAdmin):
    list_display = ("id","nome","legenda","publico")
    list_display_links = ("id","nome")
    search_fields =("nome","legenda","descricao","foto")
    list_filter = ("categoria","publico")
    list_editable = ("publico",)
    list_per_page = 10 

admin.site.register(Fotografia,ListaFotos)