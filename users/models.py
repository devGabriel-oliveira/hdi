from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        ('PACIENTE', 'Paciente'),
        ('PROFISSIONAL', 'Profissional da Saúde'),
    )

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES
    )
