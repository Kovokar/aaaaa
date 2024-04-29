from django.db import models


class Base (models.Model): 
    criacao = models.DateTimeField(auto_now_add= True) 
    atualizacao = models.DateTimeField(auto_now= True) 
    ativo = models.BooleanField(default=True) 

    class Meta: 
        abstract = True

    
class Usuarios(Base):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self) -> str:
        return self.nome
    

class Pedidos(Base):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    
    def __str__(self) -> str:
        return self.nome
    
