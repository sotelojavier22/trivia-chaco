from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Pregunta, Opcion, Respuesta

def vista_pregunta(request, id_pregunta):
    pregunta = get_object_or_404(Pregunta, orden = id_pregunta)
    return render(request, 'quiz/mostrar_pregunta.html', {'pregunta': pregunta})

