from django.shortcuts import render, HttpResponse, redirect
from .formulario import *
from .models import *
import apps.utilidades as util

def index(request):
    return HttpResponse("hola usuarios")

def crear(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            newForm = formulario.save(commit=False)
            print(formulario.cleaned_data["password"])
            newForm.password = util.encriptar(formulario.cleaned_data["password"])
            newForm.acceso = 0
            newForm.save()
            request.session["id"]=newForm.id
            request.session["nombre"]=newForm.nombre
            request.session["acceso"]=newForm.acceso
            
            return HttpResponse("<a  href='../../cursos/crear/'>crearcurso</a>") 
        else:
            
            context={
                "formularioRegistro": formulario,
                "formularioLogin":FormularioLogin()
            }
            return render(request, "index.html", context)
    else:
        context={
            "formularioRegistro": FormularioRegistro(),
            "formularioLogin":FormularioLogin()
        }
        return render(request, "index.html", context)
    
def login(request):
    if request.method == "POST":
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid(): 
            newForm = formulario.save(commit=False)  
            print("&"*90)
            esteUsuario=Usuario.objects.filter(email=newForm.email).first()
            
            
            request.session["id"] = esteUsuario.id
            request.session["nombre"] = esteUsuario.nombre  
            request.session["acceso"] = esteUsuario.acceso
            
            return redirect("../../cursos/crear/")
        else:
            context={
                "formularioRegistro": FormularioRegistro(),
                "formularioLogin": formulario,
                
            }
            return render(request, "master/index.html", context)
    else:
        context={
            "formularioRegistro": FormularioRegistro(),
            "formularioLogin": FormularioLogin(),
        }
        return render(request, "master/index.html", context)

def registrarProfesor(request):
    if request.method == "POST":
     
        formulario = FormularioRegistroProfesor(request.POST)
        if formulario.is_valid():
            newForm = formulario.save(commit=False)
            newForm.password = util.encriptar(formulario.cleaned_data["password"])
            newForm.acceso = 1 #profesor
            newForm.save()
            print(request.session)
           
            return HttpResponse("<p>profesor creado!</p><br><a  href='../../cursos/crear/'>volver</a>") 
        else:
            print("no es valido")
            context={
                "formularioRegistroProfesor": formulario,
            }
            return render(request, "usuarios/registrarProfesor.html", context)
            #######
    else:
        context={
            "formularioRegistroProfesor": FormularioRegistroProfesor()
        }
        return render(request, "usuarios/registrarProfesor.html", context)
      
      

# Create your views here.
