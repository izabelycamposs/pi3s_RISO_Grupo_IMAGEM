from django.urls import path
from core.views import cadastro_cliente, login, logout, listar_clientes, editar_clientes, index, dashboard, listar_clientes

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('cadastro-cliente/', cadastro_cliente, name='cadastro_cliente'),
    path('listar-clientes/', listar_clientes, name='listar_clientes'),
    path('editar-clientes/<int:client_id>/', editar_clientes, name='editar_clientes'),
    path('deletar-clientes/<int:client_id>/', editar_clientes, name='deletar_clientes'),
    path('cadastro-usuario/', cadastro_cliente, name='cadastro_usuario'),
    path('listar-usuarios/', listar_clientes, name='listar_usuarios'),
    path('editar-usuarios/<int:user_id>/', editar_clientes, name='editar_usuarios'),
    path('deletar-usuarios/<int:user_id>/', editar_clientes, name='deletar_usuarios'),
    path('cadastro-veiculo/', cadastro_cliente, name='cadastro_veiculo'),
    path('listar-veiculos/', listar_clientes, name='listar_veiculos'),
    path('editar-veiculos/<int:vehicle_id>/', editar_clientes, name='editar_veiculos'),
    path('deletar-veiculos/<int:vehicle_id>/', editar_clientes, name='deletar_veiculos'),
    path('cadastro-servico/', cadastro_cliente, name='cadastro_servico'),
    path('listar-servicos/', listar_clientes, name='listar_servicos'),
    path('editar-servicos/<int:service_id>/', editar_clientes, name='editar_servicos'),
    path('deletar-servicos/<int:service_id>/', editar_clientes, name='deletar_servicos'),
]
