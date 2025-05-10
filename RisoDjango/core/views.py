from django.shortcuts import render
from django.http import HttpResponse
from .services.user_services import autenticar_usuario

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if autenticar_usuario(username, password):
            return HttpResponse(f"Logado como {username}")
        return HttpResponse("Usuário ou senha inválidos", status=401)

    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

