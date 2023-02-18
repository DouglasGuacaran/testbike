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
class Proyectos(models.Model):
    Estado = models.CharField(max_length=230)
    FechaPresentacionFecha = models.CharField(max_length=255)
    Inversion = models.CharField(max_length=255)
    Mapa = models.CharField(max_length=255)
    No = models.CharField(max_length=250)
    Nombre = models.CharField(max_length=255)
    Region = models.CharField(max_length=250)
    Tipo = models.CharField(max_length=250)
    Tipologia = models.CharField(max_length=255)
    Titular = models.CharField(max_length=255)
    