from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Pedidos, Usuarios
from django.contrib.auth.decorators import login_required
from .serializers import UsuariosSerializer, PedidosSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


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
    return render(request, 'registration/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'register.html', {'error_message': 'As senhas não coincidem. Tente novamente.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Este nome de usuário já está em uso. Tente outro.'})

        if User.objects.filter(password=password).exists():
            return render(request, 'register.html', {'error_message': 'Esta senha já está em uso. Tente outra.'})
        
        user = User.objects.create_superuser(username=username, email='', password=password)
        print('id?',User.id)
        login(request, user)
        return redirect('login')  # Redirecionar para a página principal após o registro

    return render(request, 'register.html')


def home_view(request):
    return render(request, 'home.html')


@login_required    
def list_users(request):
    users = User.objects.all()
    return render(request, 'list_users.html', {'users': users})


@login_required  
def logado_view(request):
    return render(request, 'logado.html')


@login_required  
def cadastro_items(request):
    if request.method == "POST":
        nome = request.POST.get('nome_item')
        preco =request.POST.get('preco_item')

        pedidos = Pedidos(
            nome = nome,
            preco = preco,

        )

        pedidos.save()
        
    return render(request, 'itens.html')



class UsuariosListAndCreate(APIView):
    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuariosDetailAndDelete(APIView):
    def get_object(self, pk):
        try:
            return Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            raise FileNotFoundError
        
    def get(self,request ,pk):
        usuarios  =self.get_object(pk)
        serializer = UsuariosSerializer(usuarios)
        return Response(serializer.data)
    
    def put(self,request ,pk):
        usuarios = self.get_object(pk)
        serializer = UsuariosSerializer(usuarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        usuarios = self.get_object(pk)
        usuarios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PedidosListAndCreate(APIView):
    def get(self, request):
        pedidos = Pedidos.objects.all()
        serializer = PedidosSerializers(pedidos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PedidosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PedidosDetailAndDelete(APIView):
    def get_object(self, pk):
        try:
            return Pedidos.objects.get(pk=pk)
        except Pedidos.DoesNotExist:
            raise FileNotFoundError
        
    def get(self,request ,pk):
        pedidos = self.get_object(pk)
        serializer = PedidosSerializers(pedidos)
        return Response(serializer.data)
    
    def put(self,request ,pk):
        pedidos = self.get_object(pk)
        serializer = PedidosSerializers(pedidos, data=request.data)
        if serializer.ia_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request ,pk):
        pedidos = self.get_object(pk)
        pedidos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)