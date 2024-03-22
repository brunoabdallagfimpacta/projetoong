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
    cnpj = models.CharField(max_length=18)
    email = models.EmailField()
    celular = models.CharField(max_length=15)
    senha = models.CharField(max_length=255)

    @classmethod
    def criar_pj_com_usuario(cls, email, senha, nome_fantasia, **extra_fields):
        if User.objects.filter(email=email).exists():
            raise UsuarioJaExisteException(f"Já existe um usuário com o email {email}.")

        user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome_fantasia)
        return True

    def __str__(self):
        return self.nome_fantasia


@receiver(pre_save, sender=CadastroPessoaJuridica)
def hash_password(sender, instance, **kwargs):
    if instance._state.adding and instance.senha:
        instance.senha = make_password(instance.senha)
    elif not instance._state.adding:
        original = CadastroPessoaJuridica.objects.get(pk=instance.pk)
        if instance.senha != original.senha:
            instance.senha = make_password(instance.senha)