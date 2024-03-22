from django.urls import path
from .views import cadastro_empresa, cadastro_voluntario

urlpatterns = [
    path('', cadastro_voluntario, name='formulario'),
    path('cadastro-pj/', cadastro_empresa, name='formulario')
]