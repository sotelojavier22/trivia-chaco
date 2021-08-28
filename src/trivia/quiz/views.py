from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Pregunta, Opcion, Respuesta

def iniciar(request):
    return HttpResponse('<a href="../pregunta/1">Iniciar</a>')

def vista_pregunta(request, pregunta_orden):
    pregunta = get_object_or_404(Pregunta, orden = pregunta_orden)
    return render(request, 'quiz/mostrar_pregunta.html', {'pregunta': pregunta})

def responder(request, id_pregunta):
    return HttpResponse('ok')

