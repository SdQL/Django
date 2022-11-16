from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, 'formulario.html')


def buscar(request):

    if request.GET['prod']: # Validamos que en el campo si haya sido rellenado
        producto = request.GET['prod']
        if len(producto) > 20:
            mensaje = 'Texto demasiado largo'
        else:
            articulos = Articulos.objects.filter(nombre__icontains = producto)
            return render(request, 'resultados.html', {'articulos':articulos, 'query':producto})    
    else:
        mensaje = 'Intentalo de nuevo. No has llenado correctamente el campo' # En caso de que no, se retornará este mensaje
    
    return HttpResponse(mensaje) # Devolvemos lo que haya en la variable [mensaje]

def contacto(request):
    if request.method == 'POST':
        mi_formulario = FormularioContacto(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data # Guardamos la informacion el formulario en una variable
            send_mail(info['asunto'], info['mensaje'], 
            info.get('email', ''), ['sadavid2007@gmail.com'],) # Enviamos la información 

            return render(request, 'gracias.html')

    else:
        mi_formulario = FormularioContacto() # Construye el formulario, pero esta vez vacio.
        
    return render(request, 'formulario_contacto.html', {'form': mi_formulario})