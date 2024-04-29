from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('logado')  # Redirecionar para a página principal após o login
        else:
            # Se as credenciais estiverem incorretas, exibir uma mensagem de erro
            return render(request, 'login.html', {'error_message': 'Credenciais inválidas. Tente novamente.'})
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'register.html', {'error_message': 'As senhas não coincidem. Tente novamente.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Este nome de usuário já está em uso. Tente outro.'})

        user = User.objects.create_superuser(username=username, email='', password=password)
        login(request, user)
        return redirect('login')  # Redirecionar para a página principal após o registro

    return render(request, 'register.html')


def home_view(request):
    return render(request, 'home.html')

def logado_view(request):
    return render(request, 'logado.html')
