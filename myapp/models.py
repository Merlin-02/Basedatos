from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero_boleta = models.CharField(max_length=20, unique=True)
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    