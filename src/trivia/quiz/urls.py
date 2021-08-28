from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('iniciar/',views.iniciar, name='ruta_iniciar'),
    path('pregunta/<int:pregunta_orden>/', views.vista_pregunta, name='form_pregunta'),
    path('pregunta/<int:id_pregunta>/responder',views.responder, name='ruta_responder')
]