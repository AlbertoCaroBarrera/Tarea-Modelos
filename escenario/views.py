from django.shortcuts import render
from escenario.models import Proyecto
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_proyectos(request):
    proyectos = Proyecto.objects.prefetch_related("usuario").select_related("creador").all()
    return render(request, 'proyecto/lista.html',{"proyectos_mostrar":proyectos})