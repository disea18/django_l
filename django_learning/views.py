from django.http import HttpResponse
import random
from django.template import Template, Context, loader
from datetime import datetime
from django.template.loader import get_template
from django.shortcuts import render
"""
OJO: importar de django el modulo

2 objetos necesarios para realizar una petición a una URL y devolver una respuestaa traves de una vista.    
    
    # Request: para realizar peticiones al servidor.
    
    # httpResponsive: Para enviar la respuesta usando el protocolo HTTP.
    
    
    jango utiliza objetos request y response para pasar estado a través del sistema.

Cuando se solicita una página, Django crea un objeto HttpRequest que contiene metadatos sobre la solicitud. 
Entonces Django carga la vista apropiada, pasando el objeto HttpRequest como primer argumento a la función 
de la funcion vista. Cada vista es responsable de devolver un objeto HttpResponse.
    
"""


# Esto es una vista
def bienvenida(request): #>> aqui pasamos un objeto de tipo request como argumento.
    return HttpResponse ("bienvenido a este curso de Django !!! ")

def estilo_rojo(request):
    return HttpResponse("<h1 style= color:red> Este es otro estilo de prueba       </h1>")

def categoria_edad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "adultez"    
    else:
            if edad < 10: categoria = "infancia" 
            else: categoria = "adolescencia"
    resultado = " <h1> Categoria de la edad: %s</h1>" %categoria         
    return HttpResponse(resultado)
    
def random_number(request):
    numero = random.randint(1,10)
    mostrar = '<h1>Tu numero al azar es: </h1>%s' %numero
    return HttpResponse(mostrar)        

def conthtml(request, nombre, edad):
    contenido = """
    
    <!DOCTYPE html>
<html lang="en">

  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML Prueba</title>
    
  </head>
  
  <body>
	<h1> Tu nombre es: </h1> <p>%s </p>
    <p> </p>
    <h1> Tu edad es: </h1> <p>%s </p>
  </body>
</html>
    
    """%(nombre, edad)
    return HttpResponse(contenido) 

def contplant(request):
    
    #Asi se abre una plantilla llamada index alojada en la carpeta templates.
    plantillaindex = open("C:\\Users\\Daniel Alejandro\\Desktop\\django_learning\\templates\\index.html")
    # Cargar el documento en una variable de tipo plantilla.
    temp = Template(plantillaindex.read())
    # Es una buena practica cerrar el documento externo que alberga la plantilla. Asi se hace:
    plantillaindex.close()
    # Aqui creamos un contexto 
    contexto = Context()
    #Renderizar el documento:
    documento= temp.render(contexto)
    #final de todo con return y HttpResponse
    return HttpResponse(documento)
    
def plantParam(request):
    
    nombre = "Daniel"
    fecha_actual= datetime.now
       
    plantillaindex = open("C:\\Users\\Daniel Alejandro\\Desktop\\django_learning\\templates\\plantillaParametros.html")
    temp = Template(plantillaindex.read())

    plantillaindex.close()

    contexto = Context({"nombre_autor":nombre, "fecha_actual":fecha_actual})

    documento= temp.render(contexto)

    return HttpResponse(documento)
    
    
def plant_listas(request):
    
    nombre = "Daniel"
    fecha_actual= datetime.now
    lenguaje_programacion = ["Python", "Java", "Javascript","C#"]
    
       
    plantillaindex = open("C:\\Users\\Daniel Alejandro\\Desktop\\django_learning\\templates\\plantListas")

    temp = Template(plantillaindex.read())

    plantillaindex.close()

    contexto = Context({"nombre_autor":nombre, "fecha_actual":fecha_actual, "lenguajes":lenguaje_programacion})

    documento= temp.render(contexto)

    return HttpResponse(documento)  

def plant_loader(request):
    
    nombre = "Daniel"
    fecha_actual= datetime.now
    lenguaje_programacion = ["Python", "Java", "Javascript","C#"]
    
    #aqui se usa el objeto loader con el metodo get_template el cual simplifica la tarea de cargar las plantillas. 
    # sin embargo no es necesario poner el "loader." ya que lo importé y esta al principio del documento.
    plantillaExterna = loader.get_template('plantillaLoader.html').render({"nombre_autor":nombre, "fecha_actual":fecha_actual, "lenguajes":lenguaje_programacion})
    # tambien se renderiza el documento para poder agregar las variables creadas arriba(nombre, fecha_actual y lenguaje_programacion)
    # a la plantilla html.
    return HttpResponse(plantillaExterna)


def plantillaShortcut(request):
    nombre = "Daniel"
    fecha_actual= datetime.now
    lenguaje_programacion = ["Python", "Java", "Javascript","C#"]
    #aqui estamos haciendo uso del metodo render para acortar el codigo. Primero se pone request siempre y los demas parametros son
    #opcionales, aunque aqui vamos a poner el nombre de la plantilla entre '' y {"nombre_autor":nombre, "fecha_actual":fecha_actual, "lenguajes":lenguaje_programacion}
    return render(request, 'plantilla_shortcut.html',{"nombre_autor":nombre, "fecha_actual":fecha_actual, "lenguajes":lenguaje_programacion} )

def plantilla_hija1(request):
    return render(request, "plantilla_hija1.html", {})