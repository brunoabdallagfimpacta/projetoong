from django.contrib import admin
from .models import CadastroPessoaJuridica, CadastroPessoaFisica, ONG
# Register your models here.



admin.site.register(CadastroPessoaJuridica)
admin.site.register(CadastroPessoaFisica)
admin.site.register(ONG)
