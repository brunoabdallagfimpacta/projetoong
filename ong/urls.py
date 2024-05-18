from django.urls import path
from . import views

urlpatterns = [
    path('cadastro-pf/', views.cadastro_voluntario, name='formulario-pf'),
    path('cadastro-pj/', views.cadastro_empresa, name='formulario'),
    path('', views.login, name='login'),
    path('bem-vindo/', views.bem_vindo, name='bem_vindo'),
    path('cadastro-ong/',  views.cadastro_ong, name='cadastro_ong'),
    path('home/', views.home, name='home-empresa'),
    path('editar/<int:id>/', views.editar_ong, name='editar_ong'),
    path('excluir/<int:id>/', views.excluir_ong, name='excluir_ong'),
    path('cadastro-doacao/<int:ong_id>/', views.cadastro_doacao, name='cadastro_doacao'),
]