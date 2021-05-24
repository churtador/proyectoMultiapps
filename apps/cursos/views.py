from django.shortcuts import render, HttpResponse, redirect
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
        "cursosActivosTotales":Curso.objects.filter(activo=1)
    }
    return render(request, "cursos/mostrar.html", context)

def eliminarCurso(request, idCurso):
    esteCurso=Curso.objects.get(id=idCurso)
    esteCurso.activo = 0
    esteCurso.save()
    return redirect("../mostrar/")

# Create your views here.
