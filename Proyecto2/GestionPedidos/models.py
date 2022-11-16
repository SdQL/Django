from django.db import models

# Create your models here.
# Base de datos: 

# Creación de tablas de la base de datos:
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=10)

    def __str__(self):
        return f'Cliente: {self.nombre}'

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return f'Articulo: {self.nombre} | Sección: {self.seccion} | Precio: {self.precio}'

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()