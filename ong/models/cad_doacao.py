from django.db import models

class Doacao(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    nome_beneficiario = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=20)
    conta = models.CharField(max_length=20)
    ong = models.ForeignKey('ONG', on_delete=models.CASCADE, related_name='doacoes')

    def __str__(self):
        return f"{self.nome} - {self.valor}"
