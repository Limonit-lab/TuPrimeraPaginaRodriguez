from django.urls import path
from AlleyApp import views

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('buscar', views.Buscar, name="Buscar"),
    path('servicios', views.Servicios, name="Servicios"),
    path('profesionales', views.Profesionales, name="Profesionales"),
    path('proyectos', views.Proyectos, name="Proyectos"),
    path('compañias', views.Compañias, name="Compañías"),
]