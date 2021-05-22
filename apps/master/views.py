from django.shortcuts import render, HttpResponse
from apps.usuarios.formulario import * 

# Create your views here.
def index(request):
    context ={
           "formularioLogin":FormularioLogin(),
           "formularioRegistro":FormularioRegistro()
    }
    return render(request, "master/index.html", context)
    