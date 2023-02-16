from django.db import models

# Create your models here.
class BikeSantiago(models.Model):
    
    name_station=models.CharField(max_length=200, unique=True)
    total_attendance = models.IntegerField(blank=True, null=True)
    empty_slots = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)
    
    def __str__(self):
        return self.name_station
    

# class 