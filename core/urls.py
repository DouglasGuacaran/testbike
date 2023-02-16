from django.urls import path
from . views import home
from django.contrib.auth import views

urlpatterns = [
    path('', home,name='home'),
]