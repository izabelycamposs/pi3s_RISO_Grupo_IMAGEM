from django.urls import path
from core.views import cadastro_cliente, login, logout, listar_clientes, editar_clientes, index, dashboard

urlpatterns = [
    path('cadastro-cliente/', cadastro_cliente, name='cadastro_cliente'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('listar-clientes/', listar_clientes, name='listar_clientes'),
    path('editar-clientes/<int:client_id>/', editar_clientes, name='editar_clientes'),
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
]
