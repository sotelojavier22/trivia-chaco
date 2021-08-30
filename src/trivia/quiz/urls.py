from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views

app_name = 'quiz'
urlpatterns = [
    path('',views.index, name = 'ruta_index'),
    path('registrarse/', views.registrarse, name='ruta_registrarse'),
    path('', include('django.contrib.auth.urls')),
    path('iniciar/',views.iniciar, name='ruta_iniciar'),
    path('pregunta/<int:pregunta_orden>/', views.vista_pregunta, name='ruta_pregunta'),
    path('pregunta/<int:id_pregunta>/responder',views.responder, name='ruta_responder'),
    path('resultado/', views.mostrar_resultado, name='ruta_resultado'),
]
