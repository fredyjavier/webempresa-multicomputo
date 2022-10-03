from urllib import request
from django.shortcuts import render,redirect
from .forms import FormularioContacto

from django.core.mail import EmailMessage


# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto #instanciar
    if request.method=="POST":
       formulario_contacto=FormularioContacto(data=request.POST)  #rescata la informacion que se introduce en el formulario
       if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            #envio del correo por el contacto    
            email=EmailMessage("Mensaje django","El usuario {} con la direccion {} te escribe lo siguiente : \n\n {}".format(nombre,email,contenido),"",["fmonsa@misena.edu.co"],reply_to=email)
            #manejo de execciones para el envio del correo
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                  return redirect("/contacto/?invalido")  
    return render(request,"contacto/contacto.html",{'miformulario':formulario_contacto})

