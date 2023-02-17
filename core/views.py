from django.shortcuts import render
from .models import Estacion
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil import parser
import requests
from core.myFunctions import getConnection
def home(request):
    
    return render(request,'home.html')

def bike_list(request):
    estaciones = Estacion.objects.all()   
    return render(request,'bike_list.html',{'estaciones':estaciones})


def actualizar_estaciones(request):
    # Hacer una solicitud a la API y obtener los datos
    getConnection('http://api.citybik.es/v2/networks/bikesantiago')
    
    estaciones=Estacion.objects.all()
    # Redirigir a una página de confirmación de actualización
    return render(request, 'actualizar_estaciones.html',{'estaciones':estaciones})



def tarea2(request):
        
                
    return render(request,'tarea2.html',)
        