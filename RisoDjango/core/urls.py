from django.urls import path
from . import views

urlpatterns = [
    path('cadastro-cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('login/', views.login, name='login'),
]
