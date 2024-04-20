from django.db import models

class ONG(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    data_inicio = models.DateField(blank=True, null=True)  # `null=True` é necessário para campos de data
    RAMO_CHOICES = (
        ('alimento', 'Alimentício'),
        ('cultura', 'Cultural'),
        ('recreativo', 'Recreativo'),
        ('humanos', 'Direitos Humanos'),
        ('outro', 'Outro'),
    )
    ramo_atuacao = models.CharField(max_length=50, choices=RAMO_CHOICES, blank=True)
    outro_ramo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome
