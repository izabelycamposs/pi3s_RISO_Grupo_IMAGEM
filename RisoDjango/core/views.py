from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services import user_services, client_services 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if user_services.auth_user(username, password):
            return HttpResponse(f"Logado como {username}")
        return HttpResponse("Usuário ou senha inválidos", status=401)

    return render(request, 'login.html')

def cadastro_cliente(request):
    if request.method == 'POST':
        data = {
            "nome": request.POST.get('nome'),
            "documento": request.POST.get('documento'),
            "cep": request.POST.get('cep'),
            "email": request.POST.get('email'),
            "telefone": request.POST.get('telefone'),
            "telefone_residencial": request.POST.get('telefone_residencial'),
        }
        client_services.create_client(data)
        return render(request, 'cadastro_cliente.html', context={'success': True, 'data': data})
    
    if request.method == 'GET':
        return render(request, 'cadastro_cliente.html', context={'success': False})
