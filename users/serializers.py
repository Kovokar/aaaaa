from .models import Usuarios, Pedidos
from rest_framework import serializers


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = [
            'id',
            'nome',
            'email',
        ]

class PedidosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = [
            'id',
            'nome',
            'preco',
        ]