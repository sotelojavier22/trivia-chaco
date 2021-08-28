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
    pregunta = get_object_or_404(Pregunta, pk = id_pregunta)

    if pregunta.orden >= 5:
        return HttpResponseRedirect(reverse('quiz:ruta_resultado'))
    else:
        siguiente = pregunta.orden + 1
        return HttpResponseRedirect(reverse('quiz:ruta_pregunta', args=(siguiente,)))

def mostrar_resultado(request):
    return HttpResponse("ganaste!")


