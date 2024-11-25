from django.shortcuts import render,redirect
from usuarios.forms import LoginForms,CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    #Cria uma variavel que recebe um formulario vazio
    form = LoginForms()

    if request.method == 'POST':
        #armazena as informações do formulario
        form = LoginForms(request.POST) 
        if form.is_valid():
            nome=form['nome_login'].value() #captura as informações do formulario
            senha=form['senha'].value()


        usuario =auth.authenticate(
            request,
            username = nome,
            password = senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Usuario logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Login ou senha incorreto!')
            return redirect('login')




    return render(request, 'usuarios/login.html',{'form':form})


def cadastro(request):
    #Cria um formulario vazio
    form = CadastroForms() 

    if request.method == 'POST':
         #armazena as informações do formulario
        form = CadastroForms(request.POST)
         #valida se a senha_1 é diferente da senha_2
        if form.is_valid():
            '''
            Validação da senha está sendo feita agora no forms.py
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, 'Confirmação de senha é diferente da senha digitada!')
                return redirect('cadastro')
            '''    
            #armazena nas variaveis, oque vem do formulario
            nome=form['nome_cadastro'].value() 
            email=form['email'].value()
            senha1=form['senha_1'].value()
            #verifica se o usuário já exite na  tabela
            if User.objects.filter(username=nome).exists():
                 messages.error(request,'Usuario já existe, escolha outro usuário')
                 return redirect('cadastro')
            
            if User.objects.filter(email=email).exists():
                 messages.error(request,'E-mail ja cadastrado, escolha outro e-mail')
                 return redirect('cadastro')
            
            
            #Cria o usuário na tabela do banco de dados
            usuario = User.objects.create_user(
                username=nome,
                email = email,
                password=senha1
            )
            usuario.save()
            messages.success(request, f'O usuário {nome} foi criado com sucesso')
            
            return redirect('login')
        

    return render(request, 'usuarios/cadastro.html',{'form':form})

def logout(request):
    if not request.user.is_authenticated:
        messages.error(request,'usuário não esta logado')
        return redirect('login')
    auth.logout(request)
    messages.success(request,'Usuário deslogado com sucesso')
    return redirect('login')








# Create your views here. 
