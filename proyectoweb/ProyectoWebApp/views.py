from django.shortcuts import render,HttpResponse

import ProyectoWebApp

#importar el model servicios para luego poderlos ver en la pagina de servicios
from servicios.models import Servicio
from carro.carro import Carro


# Create your views here.

def home(request):
    carro=Carro(request)
    return render(request,"ProyectoWebApp/home.html")










