from django.urls import path
from .views import cadastro_empresa, cadastro_voluntario, login, bem_vindo, cadastro_ong

urlpatterns = [
    path('', cadastro_voluntario, name='formulario'),
    path('cadastro-pj/', cadastro_empresa, name='formulario'),
    path('login/', login, name='login'),
    path('bem-vindo/', bem_vindo, name='bem_vindo'),
    path('cadastro-ong/',  cadastro_ong, name='cadastro_ong')
]