from django.shortcuts import render
from AlleyApp import models, forms
# Create your views here.

def Inicio(request):
    return render(request, 'AlleyApp\Inicio.html')

def Servicios(request):
    if request.method == 'POST':
        formulario = forms.Form_Servicios(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            servicio = models.Servicios(nombre=informacion["nombre"], descripcion=informacion["descripcion"])
            servicio.save()
            return render(request, 'AlleyApp/Servicios.html')
    else:
        formulario = forms.Form_Servicios()
        contexto = {"formulario": formulario}
        return render(request, "AlleyApp/Servicios.html", contexto)
      
def Profesionales(request):
    if request.method == 'POST':
        formulario = forms.Form_Profesionales(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesional = models.Profesionales(nombre=informacion["nombre"], titulo=informacion["titulo"], email=informacion["email"])
            profesional.save()
            return render(request, 'AlleyApp/Profesionales.html')
    else:
        formulario = forms.Form_Profesionales()
        contexto = {"formulario": formulario}
        return render(request, "AlleyApp/Profesionales.html", contexto)
    return render(request, 'AlleyApp/Profesionales.html')    

def Proyectos(request):
    if request.method == 'POST':
        formulario = forms.Form_Proyectos(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            proyecto = models.Proyectos(nombre=informacion["nombre"], inicio=informacion["inicio"], finalizacion=["finalizacion"],
                                        actualidad=informacion["actualidad"], url_proyecto=informacion["url_proyecto"])
            proyecto.save()
            return render(request, 'AlleyApp/Proyectos.html')
    else:
        formulario = forms.Form_Proyectos()
        contexto = {"formulario": formulario}
        return render(request, "AlleyApp/Proyectos.html", contexto)
    return render(request, 'AlleyApp/Proyectos.html') 
  
def Compañias(request):
    if request.method == 'POST':
        formulario = forms.Form_Compañías(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            compañia = models.Compañías(nombre=informacion["nombre"], inicio=informacion["inicio"], fin=informacion["fin"],
                                        actualidad=informacion["actualidad"])
            compañia.save()
            return render(request, 'AlleyApp/Compañias.html')
    else:
        formulario = forms.Form_Compañías()
        contexto = {"formulario": formulario}
        return render(request, "AlleyApp/Compañias.html", contexto)
    return render(request, 'AlleyApp/Compañias.html')  

def Buscar(request):
  if request.GET['nombre']:
    nombre = request.GET['nombre']
    Compañias = models.Compañias.objects.filter(compañia__icontains=nombre)
    return render(request, 'AppCoder/Inicio.html', {'nombre': nombre})
  else:
    respuesta = 'No enviaste datos'
  
  return render(request, 'AppCoder/Inicio.html', {'respuesta': respuesta})