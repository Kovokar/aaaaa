from django.contrib import admin
from .models import Usuarios, Pedidos

@admin.register(Usuarios) 
class UsuariosAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'email', 'criacao', 'atualizacao', 'ativo') 

@admin.register(Pedidos) 
class PedidosAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'preco', 'criacao', 'atualizacao', 'ativo') 
