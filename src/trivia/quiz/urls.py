from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('iniciar/',views.iniciar, name='ruta_iniciar'),
    path('pregunta/<int:pregunta_orden>/', views.vista_pregunta, name='ruta_pregunta'),
    path('pregunta/<int:id_pregunta>/responder',views.responder, name='ruta_responder'),
    path('resultado/', views.mostrar_resultado, name='ruta_resultado'),
]
