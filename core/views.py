from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    if response.status_code == 200:
        response_json = response.json()
        
    return render(request,'home.html',{'response':response_json})

