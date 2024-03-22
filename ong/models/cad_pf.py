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
    cpf = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=15)
    senha = models.CharField(max_length=255)

    @classmethod
    def criar_voluntario_com_usuario(cls, email, senha, first_name,  last_name, **extra_fields):
        if User.objects.filter(email=email).exists():
            raise UsuarioJaExisteException(f"Já existe um usuário com o email {email}.")

        user = User.objects.create_user(username=email,  email=email, password=senha, first_name=first_name, last_name=last_name)
        return True

    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome}"


@receiver(pre_save, sender=CadastroPessoaFisica)
def hash_password(sender, instance, **kwargs):
    if instance._state.adding and instance.senha:
        instance.senha = make_password(instance.senha)
    elif not instance._state.adding:
        original = CadastroPessoaFisica.objects.get(pk=instance.pk)
        if instance.senha != original.senha:
            instance.senha = make_password(instance.senha)