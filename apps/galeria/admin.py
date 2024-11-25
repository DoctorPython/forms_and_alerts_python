from django.contrib import admin

from apps.galeria.models import Fotografia

# Register your models here.

class ListantoFotografias(admin.ModelAdmin):

    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome", "legenda")
    search_fields = ("nome",) # realiza a pesquisa pelo nome
    list_editable=("publicada",)
    list_filter=("categoria", "usuario",)
    list_per_page = 10
    





admin.site.register(Fotografia,ListantoFotografias)
 