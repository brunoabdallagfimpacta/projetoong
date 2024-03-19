from django import forms
import re


class cadastro(forms.Form):
    primeiro_nome = forms.CharField(label="Your name", max_length=100)
    segundo_nome = forms.CharField(label="Your last name", max_length=100)
    cpf = forms.CharField(label="CPF", max_length=11)
    email = forms.EmailField(label="Email", max_length=100)
    telefone = forms.CharField(label="Telefone")
    senha = forms.CharField(widget=forms.PasswordInput(), label="Senha")

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not re.match(r'\d{11}', cpf) or not self.valida_cpf(cpf):
            raise forms.ValidationError("CPF inválido. Por favor, insira um CPF válido.")
        return cpf

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if not any(char.isdigit() for char in senha):
            raise forms.ValidationError("A senha deve conter pelo menos um número.")
        if not any(char.isupper() for char in senha):
            raise forms.ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
        if not any(char.islower() for char in senha):
            raise forms.ValidationError("A senha deve conter pelo menos uma letra minúscula.")
        return senha

    def valida_cpf(self, cpf):
        # Adicione aqui a lógica para validar o CPF
        # Este é um espaço reservado para a implementação do algoritmo de validação de CPF
        return True  # Modifique esta linha de acordo com a lógica de validação do CPF

