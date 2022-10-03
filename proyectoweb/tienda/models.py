from distutils.command.upload import upload
from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.

#modelo categorias 

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre 

class Producto (models.Model):
    marca=models.CharField(max_length=50)
    categoria=models.ForeignKey(CategoriaProd,on_delete=models.CASCADE)#traer datos en la llave foranea y sean eliminados en cascada cuando se borren
    imagen=models.ImageField(upload_to="tienda",null=True,blank=True)
    modelo=models.CharField(max_length=50)
    caracteristicas=models.CharField(max_length=200)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"

    def __str__(self):
        return self.marca  