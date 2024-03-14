from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    ADMIN = 'admin'
    USER = 'empleado'
    ROLE_CHOICES = [
        (ADMIN, 'Administrator'),
        (USER, 'Empleado'),
    ]

    rol = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False, blank=False)

    def __str__(self) -> str:
        return self.rol


class User(AbstractUser):
    email= models.CharField(max_length=100, blank=False, null=False, unique=True)
    nombre= models.CharField(max_length=100, blank=False, null=False)
    telefono= models.CharField(max_length=100, blank=False, null=False)
    rol= models.ForeignKey(Role, on_delete=models.CASCADE, blank=False, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']