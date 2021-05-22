from django.shortcuts import render, HttpResponse
from .formulario import *

def index(request):
    return HttpResponse("bienvenido a cursos")

def crear(request):
    if request.method == "POST":
     
        formulario = FormularioCurso(request.POST)
        if formulario.is_valid():
            formulario.save() 
            print("cursocreado")
            context={
           
            "cursosTotales": Curso.objects.all(),
            "formularioCurso": FormularioCurso(),
        }
            return render(request, "cursos/crearCurso.html", context)
        else:
            context={
                "formularioCurso": formulario,
                "cursosTotales": Curso.objects.all()
            }
            return render(request, "cursos/crearCurso.html", context)
    else:
        context={
            "formularioCurso": FormularioCurso(),
            "cursosTotales": Curso.objects.all()
        }
        return render(request, "cursos/crearCurso.html", context)
    
def mostrar(request):
    context={
        "cursosTotales":Curso.objects.all()
    }
    return render(request, "cursos/mostrar.html", context)


# Create your views here.
