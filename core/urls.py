from django.urls import path
from . views import home, bike_list, tarea2, actualizar_estaciones


urlpatterns = [
    path('', home,name='home'),
    path('bike_list', bike_list,name='bike_list'),
    path('actualizar-estaciones/', actualizar_estaciones, name='actualizar_estaciones'),    
    path('tarea2/',tarea2,name='tarea2'),
]