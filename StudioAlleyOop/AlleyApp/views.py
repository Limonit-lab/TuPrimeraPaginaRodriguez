from django.shortcuts import render
from AlleyApp import models, forms
# Create your views here.

def inicio(request):
    return render(request, 'AlleyApp/inicio.html')

def Servicios(request):
    if request.method == 'POST':
        formulario = forms.Form_Servicios(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            servicio = models.Servicios(nombre=informacion["nombre"], descripcion=informacion["descripcion"])
            servicio.save()
            return render(request, 'AlleyApp/servicios.html')
    else:
        formulario = forms.Form_Servicios()
        contexto = {"formulario": formulario}
        return render(request, "AlleyApp/servicios.html", contexto)
      
def Profesionales(request):
    return render(request, 'AlleyApp/profesionales.html')    

def Proyectos(request):
    return render(request, 'AlleyApp/proyectos.html') 
  
def Compañias(request):
    return render(request, 'AlleyApp/compañias.html') 

def Buscar(request):
    return render(request, 'AlleyApp/inicio.html')  