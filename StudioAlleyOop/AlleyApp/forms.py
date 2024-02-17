from django import forms
from .models import Servicios

class Form_Servicios(forms.Form):
    servicio = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)

class Form_Profesionales(forms.Form):
    nombre = forms.CharField(max_length=30)
    titulo = forms.CharField(max_length=30)
    email = forms.EmailField()

class Form_Proyectos(forms.Form):
    nombre = forms.CharField(max_length=50)
    inicio = forms.DateField()
    finalizacion = forms.DateField()
    actualidad = forms.BooleanField ()
    url_proyecto = forms.URLField()  

class Form_Compañías(forms.Form):
    nombre = forms.CharField(max_length=30)
    inicio = forms.DateField()
    fin = forms.DateField()
    actualidad = forms.BooleanField()
    