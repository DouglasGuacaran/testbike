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