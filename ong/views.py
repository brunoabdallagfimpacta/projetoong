from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import EmpresaForm, VoluntarioForm
from .models import CadastroPessoaFisica, CadastroPessoaJuridica
from .utils import UsuarioJaExisteException


# Create your views here.
def cadastro_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            try:
                sucesso = CadastroPessoaJuridica.criar_pj_com_usuario(
                    email=form.cleaned_data['email'],
                    senha=form.cleaned_data['senha'],
                    nome_fantasia=form.cleaned_data['nome_fantasia']
                )
                if sucesso:
                    form.save()
                    return redirect('/')
            except UsuarioJaExisteException as e:
                form.add_error(None, str(e))
    else:
        form = EmpresaForm()

    return render(request, 'cad_cnpj.html', {'form': form})

def cadastro_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            try:
                sucesso = CadastroPessoaFisica.criar_voluntario_com_usuario(
                    email=form.cleaned_data['email'],
                    senha=form.cleaned_data['senha'],
                    first_name=form.cleaned_data['primeiro_nome'],
                    last_name=form.cleaned_data['sobrenome']
                )
                if sucesso:
                    form.save()
                    return redirect('/')
            except UsuarioJaExisteException as e:
                form.add_error(None, str(e))
    else:
        form = VoluntarioForm()
    return render(request, 'cad_cpf.html', {'form': form})
