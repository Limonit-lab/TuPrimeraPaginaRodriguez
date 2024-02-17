from django.db import models

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

class Profesionales(models.Model):
    nombre = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    email = models.EmailField()

class Proyectos(models.Model):
    nombre = models.CharField(max_length=50)
    inicio = models.DateField()
    finalizacion = models.DateField()
    actualidad = models.BooleanField ()
    url_proyecto = models.URLField()  

class Compañías(models.Model):
    nombre = models.CharField(max_length=30)
    inicio = models.DateField()
    fin = models.DateField()
    actualidad = models.BooleanField()
    