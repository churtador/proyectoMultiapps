from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inscripciones"),
    path("crear/", views.crear, name="inscribirse"),
    path("mostrar/", views.mostrar, name="mostrar"),
    path("misCursos/", views.misCursos, name="misCursos"),
    path("eliminarInscripcion/<int:idInscripcion>", views.eliminarInscripcion, name="eliminarInscripcion"),
]
