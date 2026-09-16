from django.conf import settings
from django.db import models

from apps.commons.models import BaseModel


class Categoria(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Local(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Objeto(BaseModel):
    STATUS_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("DEVOLVIDO", "Devolvido"),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDENTE",
    )

    foto = models.ImageField(
        upload_to="objetos/",
        blank=True,
        null=True,
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="objetos",
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="objetos",
    )

    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
        related_name="objetos",
    )

    def __str__(self):
        return self.nome