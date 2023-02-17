from django.db import models
# Create your models here.
class BikeSantiago(models.Model):
    
    id_station = models.CharField(max_length=200, unique=True)
    name_station = models.CharField(max_length=200, null=True)
    free_bikes = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)
    
    def __str__(self):
        return self.name_station
    

# class 