from django.db import models
# Create your models here.
class Estacion(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()
    bicicletas_disponibles = models.IntegerField()
    espacios_disponibles = models.IntegerField()
    ultima_actualizacion = models.DateTimeField()

    def __str__(self):
        return self.nombre
    

# class 
class Project(models.Model):
    No = models.IntegerField()
    Nombre = models.CharField(max_length=255)
    Tipo = models.CharField(max_length=10)
    Región = models.CharField(max_length=20)
    Tipología = models.CharField(max_length=5)
    Titular = models.CharField(max_length=255)
    Inversión = models.DecimalField(max_digits=10, decimal_places=4)
    FechaPresentaciónFecha = models.DateField()
    Estado = models.CharField(max_length=30)
    Mapa = models.CharField(max_length=255)
