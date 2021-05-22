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
          
            newForm.save()
            request.session["id"]=newForm.id
            request.session["nombre"]=newForm.nombre
            print(request.session)
           
            return redirect("../../cursos/crear/")
        else:
            print("no es valido")
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
    if request.method =="POST":
        formularioLogin = FormularioLogin(request.POST)
        
        if formularioLogin.is_valid():
            print("view login")
            print(formularioLogin.id)
            esteUsuario=Usuario.objects.filter(email=formularioLogin.email).first()
            request.session["id"]=esteUsuario.id
            request.session["nombre"]=esteUsuario.nombre
            return redirect("../../cursos/crear/")
        else:
            context={
                "formularioRegistro": FormularioRegistro(),
                "formularioLogin": formularioLogin,
                
            }
            return render(request, "index.html", context)
    else:
        context={
            "formularioRegistro": FormularioRegistro(),
            "formularioLogin": FormularioLogin(),
        }
        return render(request, "index.html", context)
    

# Create your views here.
