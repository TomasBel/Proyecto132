from ProyectoCoder.views import buscar, busquedaProfes, entregables, estudiantes, formulario1, formulario2, inicio, profesores, curso1, cursoFormulario
from django.urls import path
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("profesores/", profesores, name="Profesores"),
    path("entregables/", entregables, name="Entregables"),
    path("formulario/", formulario1, name="Formularios"),
    path("formulario2/", formulario2),
    path("busquedaProfes/", busquedaProfes),
    path("buscar/", buscar),
    path("cursoFormulario", cursoFormulario, name="CursoFormulario")
    ]