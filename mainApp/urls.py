from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('agregarActividad', views.agregarActividadTutorial, name='agregarActividad'),

]