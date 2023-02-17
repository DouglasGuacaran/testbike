from django.urls import path
from . views import home, tarea2
from django.contrib.auth import views

urlpatterns = [
    path('', home,name='home'),
    path('tarea2/',tarea2,name='tarea2')
]