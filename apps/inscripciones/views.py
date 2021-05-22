from django.shortcuts import render, HttpResponse, redirect
from .formulario import *
from .models import *
from apps.usuarios.models import *

def index(request):
    return HttpResponse("inscripciones")

def crear(request):
    if request.method == "POST":
        formulario = FormularioInscripcion(request.POST)
        print("%"*90)
        if formulario.is_valid():
            print(formulario.__dict__)
            formulario.save()
            
            return redirect("../../cursos/crear/")
        else:
            print("no es valido")
            context={
                "formularioInscripcion":formulario
            }
            return render(request, "inscripciones/inscribir.html", context)
    else:
        context={
            "formularioInscripcion": FormularioInscripcion(),
        }
        return render(request, "inscripciones/inscribir.html", context)
    
def mostrar(request):
    context={
        "inscripcionesTotales":Inscripcion.objects.all()
    }
    return render(request, "inscripciones/mostrar.html", context)

def misCursos(request):
    esteUsuario=Usuario.objects.filter(id=request.session["id"]).first()
    context={
        "misCursos":Inscripcion.objects.filter(participante__id=esteUsuario.id)
    }
    return render(request, "inscripciones/misCursos.html", context)

def eliminarInscripcion(request, idCurso):
    pass
# Create your views here.
