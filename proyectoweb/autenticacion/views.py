from operator import is_
from django.shortcuts import render,redirect
from django.views.generic import View
#clase para el formulario
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.
'''def autenticacion(request):
    return render(request,"registro/registro.html")'''

class Vregistro(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self,request):
        form=UserCreationForm(request.POST)

        if form.is_valid(): #si el formulario es valido y no contiene errores
            usuario=form.save()  #guarda la informacion en la tabla de usuarios 
            login(request,usuario) #verifica si esta logeado o no
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,"registro/registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario,password=contra) #autentica el usuario digitado con el de la base de datos
            if usuario is not None: #si el usuario existe
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request,"Usuario no existe")    
        else:
                messages.error(request,"Informacion incorrecta")          
    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})