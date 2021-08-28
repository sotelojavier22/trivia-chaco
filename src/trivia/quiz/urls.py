from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('iniciar/',views.iniciar, name='ruta_iniciar'),

    path('pregunta/<int:id_pregunta>/', views.vista_pregunta, name='form_pregunta'),
]