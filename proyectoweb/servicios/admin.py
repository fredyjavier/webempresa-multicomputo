from pyexpat import model
from django.contrib import admin
from .models import Servicio # se importa el modelo que esta en la misma carpeta

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Servicio,ServicioAdmin)