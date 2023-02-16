from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    responses = response.json()
    status= response.status_code
    return render(request,'home.html',{'response':responses,'status':status})