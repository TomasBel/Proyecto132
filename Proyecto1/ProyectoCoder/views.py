from calendar import c
from re import template
from ast import MatchMapping
from unicodedata import name
from django.http import HttpResponse
from django.template import Template,  Context
from ProyectoCoder.models import MiFamily, entregable, profesor, estudiantes1
from django.shortcuts import render
from ProyectoCoder.forms import *

def probandoTemplate(self):

	miHtml = open("C:/Users/tomas/Desktop/Python/Proyecto1/Proyecto1/Plantillas/template1.html")

	plantilla = Template(miHtml.read())

	miHtml.close()

	miContexto = Context()

	documento = plantilla.render(miContexto)

	return HttpResponse(documento)

def Family(request):

	mama = MiFamily(nombre = "Carina", edad = 47, fecha_nac="1975-05-16")
	mama.save()
	papa = MiFamily(nombre = "Edgar", edad = 52, fecha_nac="1970-01-26")
	papa.save()
	hermano = MiFamily(nombre = "Ignacio", edad = 10, fecha_nac="2011-11-07" )
	hermano.save()
	return render(request, "ProyectoCoder/Family.html",{"mama":mama,"papa":papa,"hermano":hermano})


def inicio(request): 

	return render(request, "ProyectoCoder/inicio.html")

def estudiantes(request):
	
	return render(request, "ProyectoCoder/estudiantes.html")

def profesores(request): 
	
	return render(request, "ProyectoCoder/profesores.html")

def entregables(request):
	
	ente1 = entregable(nombre="examen 1", fechaDeEntrega="2022-03-30")
	ente1.save()
	
	return render(request, "ProyectoCoder/entregables.html")

def formulario1(request):
	
	if request.method=="POST":

		formulario1 = FormularioProfesor(request.POST)

		if formulario1.is_valid(): 
		
			info = formulario1.cleaned_data

			ProfeF = profesor(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"], profesion=info["profesion"])

			ProfeF.save() 

			return render(request, "ProyectoCoder/inicio.html") 

	else: 
		
		formulario1=FormularioProfesor() 
	
	return render(request, "ProyectoCoder/formu1.html", {"form1":formulario1}) 
	
def formulario2(request):
	
	if request.method=="POST":

		formulario2 = FormularioEstudiantes(request.POST)

		if formulario2.is_valid(): 
		
			info = formulario2.cleaned_data

			estudianteF = estudiantes(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

			estudianteF.save() 

			return render(request, "ProyectoCoder/inicio.html") 

	else: 
		
		formulario2 = FormularioEstudiantes() 
	
	return render(request, "ProyectoCoder/formu2.html", {"form2":formulario2}) 


def busquedaProfes(requst):

	return render(requst, "ProyectoCoder/busquedaProfes.html")

def buscar(request):

	if request.GET["nombre"]:

		nombre = request.GET["nombre"]
		
		profes = profesor.objects.filter(nombre__icontains=nombre)
		
		
		return render(request, "ProyectoCoder/resultados.html", {"profes":profes, "nombre":nombre})
	
	else:
		
		mensaje = "No enviaste los datos"

	return HttpResponse(mensaje)

def curso1(request):
	return render(request, "ProyectoCoder/curso.html")

def cursoFormulario(request):
	return render(request, "ProyectoCoder/cursoFormulario.html")
