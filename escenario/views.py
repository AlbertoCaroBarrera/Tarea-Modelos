from django.shortcuts import render
from escenario.models import Proyecto, Asignacion_tarea
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_proyectos(request):
    proyectos = Proyecto.objects.prefetch_related("usuario").select_related("creador").all()
    return render(request, 'proyecto/lista.html',{"proyectos_mostrar":proyectos})

def dame_tareas_texto(request,texto_observacion):
    tareas = Asignacion_tarea.objects.filter(observaciones__contains=texto_observacion)
    return render(request, 'tareas/tareas_con_observaciones.html', {'asignaciones': tareas})

