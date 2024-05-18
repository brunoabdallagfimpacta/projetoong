from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password

from ong.utils import UsuarioJaExisteException

User = get_user_model()

class CadastroPessoaJuridica(models.Model):
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField()
    celular = models.CharField(max_length=15)
    senha = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    @classmethod
    def criar_pj_com_usuario(cls, email, senha, nome_fantasia, razao_social, cnpj, celular, **extra_fields):
        if User.objects.filter(email=email).exists():
            raise UsuarioJaExisteException(f"Já existe um usuário com o email {email}.")

        user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome_fantasia,
                                        **extra_fields)
        pj = cls(
            razao_social=razao_social,
            nome_fantasia=nome_fantasia,
            cnpj=cnpj,
            email=email,
            celular=celular,
            user=user,
            senha=make_password(senha)
        )
        pj.save()
        return pj

    def __str__(self):
        return self.nome_fantasia