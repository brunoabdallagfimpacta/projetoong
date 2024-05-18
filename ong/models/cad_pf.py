from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password

from ong.utils import UsuarioJaExisteException

User = get_user_model()
class CadastroPessoaFisica(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=15)
    senha = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    @classmethod
    def criar_voluntario_com_usuario(cls, email, senha, first_name, last_name, cpf, celular, **extra_fields):
        if User.objects.filter(email=email).exists():
            raise UsuarioJaExisteException(f"Já existe um usuário com o email {email}.")

        user = User.objects.create_user(username=email, email=email, password=senha, first_name=first_name,
                                        last_name=last_name, **extra_fields)
        pessoa_fisica = cls(
            primeiro_nome=first_name,
            sobrenome=last_name,
            cpf=cpf,
            email=email,
            celular=celular,
            user=user,
            senha=make_password(senha)
        )
        pessoa_fisica.save()
        return pessoa_fisica

    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome}"