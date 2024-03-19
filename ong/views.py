from django.shortcuts import render
from .forms import cadastro

# Create your views here.
def cadastro_pf(request):
    context = {
        'cadastro': cadastro
    }
    if request.method == 'POST':
        form = cadastro(request.POST)

        if form.is_valid():
            pass

    return render(request, 'cad_cpf.html', context=context)


def cadastro_pj(request):
    context = {
        'cadastro': cadastro
    }
    if request.method == 'POST':
        form = cadastro(request.POST)

        if form.is_valid():
            pass

    return render(request, 'cad_cnpj.html', context=context)