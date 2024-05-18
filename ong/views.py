from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpresaForm, VoluntarioForm, CustomLoginForm, ONGForm, DoacaoForm
from .models import CadastroPessoaFisica, CadastroPessoaJuridica, ONG
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
        if form.is_valid():
            cpf_cnpj = request.POST.get('username')
            password = request.POST.get('password')

            acesso = None
            try:
                acesso = CadastroPessoaFisica.objects.get(cpf=cpf_cnpj)
            except CadastroPessoaFisica.DoesNotExist:
                try:
                    acesso = CadastroPessoaJuridica.objects.get(cnpj=cpf_cnpj)
                except CadastroPessoaJuridica.DoesNotExist:
                    pass

            if acesso is not None:
                user = authenticate(username=acesso.user.username, password=password)
                if user is not None:
                    print('Usuário autenticado:', user.username)
                    django_login(request, user)
                    return redirect('home-empresa')
                else:
                    form.add_error("password", "Usuário ou senha incorretos")
            else:
                form.add_error("username", "Usuário não encontrado")
        else:
            print("Formulário inválido:", form.errors)
    else:
        form = CustomLoginForm()

    return render(request, 'formulario.html', {'form': form})

def bem_vindo(request):
    if request.user.is_authenticated:
        return render(request, 'bem-vindo.html', {'user': request.user})
    else:
        return redirect('login')


def cadastro_ong(request):
    if request.method == 'POST':
        form = ONGForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')  # Redirecione para a página inicial ou uma página de sucesso
        else:
            print(form.errors)  # Isso ajudará a ver quais erros estão sendo gerados, se houver
    else:
        form = ONGForm()

    return render(request, 'cadastro_ong.html', {'form': form})
@login_required
def home(request):
    dados = ONG.objects.all()
    return render(request, 'index_lista.html', {'dados': dados})

@login_required
def editar_ong(request, id):
    ong = get_object_or_404(ONG, id=id)
    if request.method == "POST":
        form = ONGForm(request.POST, instance=ong)
        if form.is_valid():
            form.save()
            return redirect('home-empresa')
    else:
        form = ONGForm(instance=ong)
    return render(request, 'editar_ong.html', {'form': form})

@login_required
def excluir_ong(request, id):
    ong = get_object_or_404(ONG, id=id)
    ong.delete()
    return redirect('home-empresa')


def cadastro_doacao(request, ong_id):
    ong = get_object_or_404(ONG, id=ong_id)

    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            doacao = form.save(commit=False)
            doacao.ong = ong
            doacao.save()
            return redirect('/home/')  # Redirecione para a página inicial ou uma página de sucesso
        else:
            print(form.errors)  # Isso ajudará a ver quais erros estão sendo gerados, se houver
            print(request.POST)  # Verificar o conteúdo do POST
    else:
        form = DoacaoForm()

    return render(request, 'tela_pagamento.html', {'form': form, 'ong': ong})