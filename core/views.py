from django.shortcuts import render
from .models import BikeSantiago
import requests

def home(request):
    datos = BikeSantiago.objects.values()
    if datos == 0:
        url = 'http://api.citybik.es/v2/networks/bikesantiago'
        response = requests.get(url)
        data = response.json()
        
        for i in data['network']['stations']:
            datos_bikesantiago = BikeSantiago(
                id_station = i['id'],
                name_station = i['name'],
                free_bikes = i['free_bikes'],
                address = i['extra']['address'],
                latitude = i['latitude'],
                longitude = i['longitude']
            )
        
            datos_bikesantiago.save()
            all_data = BikeSantiago.objects.all().order_by('-id')
    else:
        all_data = BikeSantiago.objects.all().order_by('latitude')
    return render(request,'home.html',{"all_data":all_data})


