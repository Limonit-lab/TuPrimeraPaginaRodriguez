from django.shortcuts import render
from AlleyApp import models
# Create your views here.





from django.shortcuts import render
#from AppCoder import forms, models

def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def cursos(request):
    if request.method == 'POST':
        formulario = forms.Form_Curso(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            curso = models.Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, 'AppCoder/cursos.html')
    else:
        formulario = forms.Form_Curso()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/cursos.html", contexto)
    

def profesores(request):
    return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')


def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def buscar(request):
  if request.GET['camada']:
    camada = request.GET['camada']
    cursos = models.Curso.objects.filter(camada__icontains=camada)
    return render(request, 'AppCoder/inicio.html', {'cursos': cursos, 'camada': camada})
  else:
    respuesta = 'No enviaste datos'
  
  return render(request, 'AppCoder/inicio.html', {'respuesta': respuesta})