from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('agregarActividad', views.agregarActividadTutorial, name='agregarActividad'),
    path('editarActividad', views.editarActividadTutorial, name='editarActividad'),
    path('infoActividad', views.infoActividadTutorial, name='infoActividad'),
    path('evaluarTutor', views.infoEvaluarTutor, name='infoTutor'),
    path('atencionIndividual',views.infoatencionIndividual, name='atencionIndividual'),
    path('editarAtencion',views.infoeditarAtencion, name='editarAtencion'),
    path('registrarAtencion',views.inforegistrarAtencion, name='registrarAtencion')

]