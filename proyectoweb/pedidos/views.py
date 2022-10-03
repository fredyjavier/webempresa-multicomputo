from email import message
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages

from pedidos.models import LienaPedido, Pedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objet.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LienaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    LienaPedido.objects.bulk_create(lineas_pedido)
    

    #enviamos mail al cliente
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email  

    )  
    messages.success(request,"Elpedido se a creado")
    return redirect('../tienda')

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario") 
                       
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="fredy.moncaleano@gmail.com"
    to=kwargs.get("fmonsa@misena.edu.co")
    #to="aquí la dirección del destinatario"

    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)