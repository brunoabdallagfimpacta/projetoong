from django.urls import path
from .views import cadastro_empresa, cadastro_voluntario, login

urlpatterns = [
    path('', cadastro_voluntario, name='formulario'),
    path('cadastro-pj/', cadastro_empresa, name='formulario'),
    path('login/', login, name='login')
]