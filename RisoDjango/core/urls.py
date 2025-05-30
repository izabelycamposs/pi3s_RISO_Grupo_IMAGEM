from django.urls import path
from . import views

urlpatterns = [
    path('cadastro-cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('listar-clientes/', views.listar_clientes, name='listar_clientes'),
    path('editar-clientes/<int:client_id>/', views.editar_clientes, name='editar_clientes'),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
