from django import forms
from .models import CadastroPessoaFisica, CadastroPessoaJuridica

class EmpresaForm(forms.ModelForm):
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")

    class Meta:
        model = CadastroPessoaJuridica
        fields = ['razao_social', 'nome_fantasia', 'cnpj', 'email', 'celular', 'senha']
        widgets = {
            'razao_social': forms.TextInput(attrs={'placeholder': 'Digite a Razão Social'}),
            'nome_fantasia': forms.TextInput(attrs={'placeholder': 'Digite o Nome Fantasia'}),
            'cnpj': forms.TextInput(attrs={
                'placeholder': 'xx.xxx.xxx/xxxx-xx',
                'pattern': '\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}',
                'title': 'Digite o CNPJ no formato: xx.xxx.xxx/xxxx-xx',
                'onchange': 'formatarCNPJ(this)'
            }),
            'email': forms.EmailInput(attrs={'placeholder': 'Email@email.com.br'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Digite o seu celular (00) 0 0000-0000', 'onchange': 'formatarCelular(this)'}),
            'senha': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', "As senhas não coincidem")

        return cleaned_data


class VoluntarioForm(forms.ModelForm):
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Senha")

    class Meta:
        model = CadastroPessoaFisica
        fields = ['primeiro_nome', 'sobrenome', 'cpf', 'email', 'celular', 'senha']
        widgets = {
            'primeiro_nome': forms.TextInput(
                attrs={'placeholder': 'Digite seu primeiro nome', 'id': 'id_primeiro_nome'}
            ),
            'sobrenome': forms.TextInput(attrs={'placeholder': 'Digite seu sobrenome', 'id': 'id_sobrenome'}),
            'cpf': forms.TextInput(attrs={
                'placeholder': 'xxx.xxx.xxx-xx',
                'id': 'id_cpf',
                'pattern': '\d{3}\.?\d{3}\.?\d{3}-?\d{2}',
                'onchange': 'formatarCPF(this)'
            }),
            'email': forms.EmailInput(attrs={'placeholder': 'Email@email.com.br', 'id': 'id_email'}),
            'celular': forms.TextInput(attrs={
                'placeholder': '(00) 90000-0000',
                'id': 'id_celular',
                'onchange': 'formatarCelular(this)'
            }),
            'senha': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'id': 'id_senha'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', "As senhas não coincidem")

        return cleaned_data


class CustomLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))