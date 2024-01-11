from django.db import models


class Empleado(models.Model):
    dni= models.CharField(blank=False, null=False, max_length=20)
    nombre= models.CharField(blank=False, null=False, max_length=100)
    cargo= models.CharField(blank=False, null=False, max_length=100)

    def __str__(self) -> str:
        return self.nombre

