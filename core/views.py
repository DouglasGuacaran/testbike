from django.shortcuts import render
from .models import Estacion
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil import parser
import requests

def home(request):
    
    return render(request,'home.html')

def bike_list(request):
    estaciones = Estacion.objects.all()   
    return render(request,'bike_list.html',{'estaciones':estaciones})


def actualizar_estaciones(request):
    # Hacer una solicitud a la API y obtener los datos
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    data = response.json()

    # Procesar los datos y actualizar los registros en la base de datos
    estaciones = data['network']['stations']
    for estacion in estaciones:
        # Comprobar si la estación ya existe en la base de datos
        try:
            obj = Estacion.objects.get(id=estacion['id'])
        except Estacion.DoesNotExist:
            obj = Estacion(id=estacion['id'])

        # Actualizar los campos de la estación
        obj.nombre = estacion['name']
        obj.latitud = estacion['latitude']
        obj.longitud = estacion['longitude']
        obj.bicicletas_disponibles = estacion['free_bikes']
        obj.espacios_disponibles = estacion['empty_slots']
        obj.ultima_actualizacion = parser.parse(estacion['timestamp'])

        # Guardar la estación en la base de datos
        obj.save()
    estaciones=Estacion.objects.all()
    # Redirigir a una página de confirmación de actualización
    return render(request, 'actualizar_estaciones.html',{'estaciones':estaciones})



def tarea2(request):
    soup = BeautifulSoup(requests.get("https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php").text, "html.parser")
    table = soup.find('table')
    data_json = {}
    header = []
    rows = []
    for i, row in enumerate(table.find_all('tr')):
        if i == 0:
            header = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])
    print(header)
   
    for row in rows:
        print(row)
    print(data_json+'JOOO')
    
                
    return render(request,'tarea2.html',)
        