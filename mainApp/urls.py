from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('agregarActividad', views.agregarActividadTutorial, name='agregarActividad'),
    path('editarActividad', views.editarActividadTutorial, name='editarActividad'),
    path('infoActividad', views.infoActividadTutorial, name='infoActividad'),
]