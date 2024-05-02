# urls.py

from django.urls import path
from .views import login_view, register_view, home_view, logado_view, list_users,cadastro_items



urlpatterns = [
    path('login/', login_view, name='login'),
    #path('', include('users.urls')),
    path('register/', register_view, name='register'),
    path('', home_view , name='home'),
    path('logado/',logado_view, name='logado'),
    path('list_users/', list_users, name='list_users'),
    path('itens/', cadastro_items, name='itens'),
    # Outras URLs da sua aplicação...
]
