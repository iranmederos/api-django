from django.db import models


class Empleado(models.Model):
    dni= models.CharField(blank=False, null=False, max_length=20)
    nombre= models.CharField(blank=False, null=False, max_length=100)
    cargo= models.CharField(blank=False, null=False, max_length=100)
    sueldo= models.FloatField(blank=False, null=False, default=0)
    area_asignada = models.ForeignKey('Area', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nombre

class Tarea(models.Model):
    concepto= models.CharField(blank=False, null=False, max_length=50)
    descripcion= models.CharField(blank=False, null=False, max_length=200)
    f_inicio= models.DateField()
    f_fin= models.DateField()
    empleado= models.ForeignKey(Empleado, on_delete=models.CASCADE)


class Area(models.Model):
    nombre= models.CharField(blank=False, null=False, max_length=100)
    capacidad= models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    empleados = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class Maquina(models.Model):
    marca= models.CharField(blank=False, null=False, max_length=100)
    modelo= models.CharField(blank=False, null=False, max_length=100)
    empleados_operadores= models.ManyToManyField(Empleado)