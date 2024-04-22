from django.db import models

# Create your models here.

class Cuerda(models.Model):
    Serie_producto = models.CharField(max_length=50)
    tipo =  models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)    
    Disponible = models.BooleanField()
    fecha = models.DateTimeField(auto_now=True)
    valor = models.IntegerField()



class Percusion(models.Model):
    Serie_producto = models.CharField(max_length=50)
    tipo =  models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)    
    Disponible = models.BooleanField()
    fecha = models.DateTimeField(auto_now=True)
    valor = models.IntegerField()



class Amplificador(models.Model):
    Serie_producto = models.CharField(max_length=50)
    tipo =  models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)    
    Disponible = models.BooleanField()
    fecha = models.DateTimeField(auto_now=True)
    valor = models.IntegerField()


class Accesorio(models.Model):
    Serie_producto = models.CharField(max_length=50)
    tipo =  models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)    
    Disponible = models.BooleanField()
    fecha = models.DateTimeField(auto_now=True)
    valor = models.IntegerField()



    
 