from django.urls import path
from .views import cadastro_pf, cadastro_pj

urlpatterns = [
    path('cadastro-pf/', cadastro_pf, name='formulario'),
    path('cadastro-pj/', cadastro_pj, name='formulario')
]