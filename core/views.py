import sys
from django.shortcuts import render
from .models import Estacion, Proyectos
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil import parser
import requests
from core.myFunctions import getConnection, obtenerData
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
    return render(request, 'bike_list.html',{'estaciones':estaciones})



def tarea2(request):
    proyectos = obtenerData()
    for proyecto in proyectos:
        
        obj = Proyectos()
        
        obj.No = proyecto['No']
        obj.Nombre = proyecto['Nombre']
        obj.Tipo = proyecto['Tipo']
        obj.Region = proyecto['Región']
        obj.Tipologia = proyecto['Tipología']
        obj.Titular = proyecto['Titular']
        obj.Inversion = proyecto['Inversión(MMU$)']
        obj.FechaPresentacionFecha = proyecto['FechaPresentaciónFecha deIngreso(*)']
        obj.Estado = proyecto['Estado']
        obj.Mapa = proyecto['Mapa']
        obj.save()
        
    proyectos=Proyectos.objects.all()
    return render(request, 'tarea2.html', {'proyectos': proyectos})

    
def actualizar_proyectos(request):
    if 'your_name' not in request.GET:
        # Inicializamos variables del template
        current_value = 1
        resultado = "nada primera carga"
    else:
        # Hacemos calculos
        current_value = request.GET['your_name']
        resultado = "resultado : " + current_value

    return render(request, 'home.html', {'resultado': resultado, 'current_value': current_value})