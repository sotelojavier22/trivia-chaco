from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .models import Pregunta, Opcion, Respuesta

def index(request):
    return render(request, 'quiz/index.html', {})
    
def registrarse(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('quiz:ruta_iniciar')
    else:
        form = UserCreationForm()
    return render(request, 'quiz/form_registro.html',{'form':form})

@login_required(login_url='/quiz/login/')
def iniciar(request):
    return render(request, 'quiz/home.html')


@login_required(login_url='/quiz/login/')
def vista_pregunta(request, pregunta_orden):
    pregunta = get_object_or_404(Pregunta, orden = pregunta_orden)

    return render(request, 'quiz/mostrar_pregunta.html', {'pregunta': pregunta})

@login_required(login_url='/quiz/login/')
def responder(request, id_pregunta):
    pregunta = get_object_or_404(Pregunta, pk = id_pregunta)
    id_usuario = request.user.id
    id_opcion = request.POST['opcion']

    print('id_pregunta', pregunta.id)
    print('id_opcion', id_opcion)

    seleccionada = pregunta.opcion_set.get(pk=id_opcion)

  
    if seleccionada.es_correcta:
        puntaje = 1
    else:
        puntaje = 0


    respuesta = Respuesta(pregunta=pregunta, opcion=seleccionada, usuario=id_usuario, puntaje=puntaje)

    respuesta.save()


    if pregunta.orden >= 5:
        return redirect(reverse('quiz:ruta_resultado'))
    else:
        siguiente = pregunta.orden + 1
        return redirect(reverse('quiz:ruta_pregunta', args=(siguiente,)))


@login_required(login_url='/quiz/login/')
def mostrar_resultado(request):
    id_usuario = request.user.id
    respuestas = Respuesta.objects.filter(usuario=id_usuario)

    puntaje_total = 0
    for r in respuestas:
       if r.puntaje == 1:
            puntaje_total += 1

    return render(request, 'quiz/resultado.html', {'puntaje': puntaje_total})

def contact(request):
    return render (request, 'quiz/contact.html')

@login_required(login_url='/quiz/login/')
def jugar(request): 
    return render (request, 'juego.html', {})

