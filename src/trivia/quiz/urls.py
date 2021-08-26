from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    #path('', views.index, name='index'),
    path('pregunta/<int:id_pregunta>/', views.vista_pregunta, name='vista_pregunta'),
    
    #path('<int:question_id>/results/', views.results, name='results'),
    
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]