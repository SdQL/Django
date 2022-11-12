from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):

    p1 = Persona('Samuel', 'Cañas')
    fecha_actual = datetime.now()
    dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dia_actual = datetime.today().strftime('%A')

    #doc_externo = open("C:/Users/Usuario/Desktop/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/index.html")
    #plantilla = Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo = get_template('index.html')

    diccionario = {'nombre_entrada':p1.nombre, 
                'apellido_entrada':p1.apellido, 
                'fecha_actual':fecha_actual,
                'dias':dias,
                'dia': dia_actual
                }
    
    #documento = doc_externo.render(plantilla)
    return render(request, 'index.html', diccionario)


def horario(request):
    fecha = datetime.now()
    return render(request, 'horario.html', {'fecha_actual':fecha})

def despedida(request):
    return HttpResponse('Adios mundo hecho con Django')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse('Hora y fecha actuales: {}'.format(fecha))

def calcula_edad(request, edad_actual, año):
    periodo = año - 2022
    edad_futura = edad_actual + periodo

    return HttpResponse('En el año {} tendrás {} años'.format(año, edad_futura))