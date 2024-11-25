from django.shortcuts import render,get_object_or_404,redirect
#from django.http import HttpResponse
from apps.galeria.models import Fotografia
from django.contrib import messages


def index(request):
    #valida se o usuário está logado, caso seja verdade redireciona para index.html, não verdade redireciona para a pagina de login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não está logado')
        return redirect('login')

    #cria o objeto foto somente se a foto estiver marcada como publicada
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
   # fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})
 

def imagem(request,foto_id): #puxa o objeto que esta salvo no banco de dados
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuário não esta logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)



    return render(request,'galeria/buscar.html', {"cards": fotografias})

# Create your views here.
