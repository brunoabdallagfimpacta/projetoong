from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import EmpresaForm, VoluntarioForm, AuthenticationForm, CustomLoginForm
from .models import CadastroPessoaFisica, CadastroPessoaJuridica
from .utils import UsuarioJaExisteException


# Create your views here.
def cadastro_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            try:
                pj = CadastroPessoaJuridica.criar_pj_com_usuario(
                    email=form.cleaned_data['email'],
                    senha=form.cleaned_data['senha'],
                    nome_fantasia=form.cleaned_data['nome_fantasia'],
                    razao_social=form.cleaned_data['razao_social'],
                    cnpj=form.cleaned_data['cnpj'],
                    celular=form.cleaned_data['celular']
                )
                if pj:
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
                pessoa_fisica = CadastroPessoaFisica.criar_voluntario_com_usuario(
                    email=form.cleaned_data['email'],
                    senha=form.cleaned_data['senha'],
                    first_name=form.cleaned_data['primeiro_nome'],
                    last_name=form.cleaned_data['sobrenome'],
                    cpf=form.cleaned_data['cpf'],  # Ensure this field is in the form
                    celular=form.cleaned_data['celular']  # Ensure this field is in the form
                )
                if pessoa_fisica:
                    return redirect('/')
            except UsuarioJaExisteException as e:
                form.add_error(None, str(e))
    else:
        form = VoluntarioForm()
    return render(request, 'cad_cpf.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        print(form)
        if form.is_valid():
            cpf_cnpj = request.POST.get('username')
            password = request.POST.get('password')

            try:
                acesso = CadastroPessoaFisica.objects.get(cpf=cpf_cnpj)
            except CadastroPessoaFisica.DoesNotExist:
                try:
                    acesso = CadastroPessoaJuridica.objects.get(cnpj=cpf_cnpj)
                except CadastroPessoaJuridica.DoesNotExist:
                    acesso = None

            if acesso is not None:
                user = authenticate(username=acesso.user.username, password=password)
                if user is not None:
                    return redirect('/')
                else:
                    form.add_error("password", "Usuário ou senha incorretos")
        else:
            print("Formulário inválido:", form.errors)
    else:
        form = CustomLoginForm(request.POST)
    return render(request, 'formulario.html', {'form': form})