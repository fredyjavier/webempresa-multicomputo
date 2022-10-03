from django.shortcuts import render
from .models import Servicio

# Create your views here.

def servicios(request):
    servicios=Servicio.objects.all() #importar todos los servicios del model pasando los parametros
    return render(request,"servicios/servicios.html",{"servicios":servicios})
