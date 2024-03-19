from django.shortcuts import render
from .forms import cadastro

# Create your views here.
def formulario(request):
    context = {
        'cadastro': cadastro
    }
    if request.method == 'POST':
        form = cadastro(request.POST)

        if form.is_valid():
            pass

    return render(request, 'cad_cpf.html', context=context)