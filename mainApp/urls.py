from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('atencion', views.obtenerCursos),
    # path('registrarCurso/', views.registrarCurso),
    # path('edicionCurso/<codigo>', views.edicionCurso),
    # path('editarCurso/', views.editarCurso),
    # path('eliminarCurso/<id>', views.eliminarCurso),
    # path('signin/', views.signin, name='signin'),
    # path('signup/', views.signup, name='signup'),
    # path('logout/', views.signout, name='logout'),
  #   path('pruebaCurso/<codigo>', views.pruebaCurso)
]