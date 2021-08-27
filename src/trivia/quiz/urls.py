from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('pregunta/<int:id_pregunta>/', views.vista_pregunta, name='vista_pregunta'),
]