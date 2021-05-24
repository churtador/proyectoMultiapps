from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cursos"),
    path("crear/", views.crear, name="crearCurso"),
    path("mostrar/", views.mostrar, name="mostrarCurso"),
    path("eliminarCurso/<int:idCurso>", views.eliminarCurso, name="eliminarCurso"),

]
