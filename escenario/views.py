from django.shortcuts import render
from escenario.models import Proyecto,Tarea, Asignacion_tarea, Comentario, Etiqueta, Usuario

# Create your views here.

def index(request):
    return render(request, 'index.html')

# 2 Crea una URL que muestre una lista de todos los proyectos de la aplicación con sus datos correspondientes.

def listar_proyectos(request):
    proyectos = Proyecto.objects.prefetch_related("usuario").select_related("creador").all()
    return render(request, 'proyecto/lista.html',{"proyectos_mostrar":proyectos})

# 3 Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por fecha de creación descendente.

def tareas(request, id_proyecto ):
    tareas = Tarea.objects.select_related("creador_tarea","proyecto").prefetch_related("usuarios_asignados")
    # filtramos por el atributo proyecto y su id, y al ordenar ponemos - para hacerlo descendente
    tareas = tareas.filter(proyecto=id_proyecto).order_by("-fecha_creacion").all()
    return render(request,"proyecto/tareas.html",{"tareas_mostrar":tareas})

# 4 Crear una URL que muestre todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente. 

def usuarios(request, id_tarea ):
    # obtenemos las tareas con su id para luego filtrar por ellas
    tarea = Tarea.objects.get(id=id_tarea) 
    usuarios = Asignacion_tarea.objects.select_related("usuario").filter(tarea=tarea).order_by("fecha_asignacion")
    return render(request,"proyecto/usuarios.html",{'mostrar_usuarios':usuarios})

# 5 Crear una URL que muestre todas las tareas que tengan un texto en concreto en las observaciones a la hora de asignarlas a un usuario.

def tareas_con_observaciones(request, texto):
    # filtramos las tareas donde el atributo observaciones de asignacion de tarea, tiene un texto. Un like en bbdd es contains.
    tarea = Tarea.objects.filter(asignacion_tarea__observaciones__contains=texto)
    return render(request, 'proyecto/tareas_con_observaciones.html', {'tareas':tarea, 'texto':texto})

# 6 -Crear una URL que muestre todos las tareas que se han creado entre dos años y el estado sea “Completada”.


def tareas_completadas_entre_años(request,fecha1,fecha2):
    # usamos year__range para decir el rango de los años , de 2000 a 2025 por ejemplo y filtramos por la tarea cuyo estado en los modelos es Co -> completada!
    tarea = Tarea.objects.filter(fecha_creacion__year__range=[fecha1,fecha2]).filter(estado='Co')
    return render(request, 'proyecto/tareas_completadas_entre_años.html',{'tareas':tarea})

# 7 Crear una URL que obtenga el último usuario que ha comentado en una tarea de un proyecto en concreto.
# le pedimos el id_tarea que tiene un proyecto asociado. Porque si pedimos un proyecto, nos saldra todos sus tareas
def ultimo_usuario_comentado(request, id_tarea):
    # filtramos las tarear por su id, ordenamos descendentemente y cojemos la primera que será la mas reciente.
    usuario = Comentario.objects.filter(tarea_id=id_tarea).order_by("-fecha_comentario")[:1].get()
    return render(request,'proyecto/ultimo_usuario_comentado.html',{'ultimo_usuario_comentado':usuario})

# 8 Crear una URL que obtenga todos los comentarios de una tarea que empiecen por la palabra que se pase en la URL y que el año del comentario sea uno en concreto.

def comentario_comienza_palabra_anyo(request, texto, anyo):
    # filtramos por un Like de bbdd con contains y el texto que queramos e igualamos la fecha del comentario al año que queramos
    comentario = Comentario.objects.filter(contenido__contains=texto).filter(fecha_comentario__year=anyo)
    return render(request,'proyecto/comentario_comienza_palabra_anyo.html',{'comentario_comienza_palabra_anyo':comentario})

# 9 Crear una URL que obtenga todas las etiquetas que se han usado en todas las tareas de un proyecto.

def etiquetas_tareas_proyecto(request,id_proyecto):
    # filtramos por el id del proyecto y mostramos todas las etiquetas
    etiqueta = Etiqueta.objects.prefetch_related("tarea").filter(tarea__proyecto_id=id_proyecto)
    return render(request,'proyecto/etiquetas_tareas_proyecto.html',{'etiquetas_tareas_proyecto':etiqueta})

# 10 Crear una URL que muestre todos los usuarios que no están asignados a una tarea.

def usuarios_sin_tarea(request, tarea_id):
    # filtramos la tarea por las que queremos con id y excluimos a los usuarios sin dicha tarea
    tarea = Tarea.objects.get(id=tarea_id)
    usuarios = Usuario.objects.exclude(asignacion_tarea__tarea=tarea)
    return render(request,'proyecto/usuarios_sin_tarea.html',{'usuarios_sin_tarea':usuarios})

# 11 Crear una página de Error personalizada para cada uno de los 4 tipos de errores que pueden ocurrir en nuestra Web.

def mi_error_404(request,exception=None):
    return render(request,'errores/404.html',None,None,404)

def mi_error_400(request,exception=None):
    return render(request,'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request,'errores/403.html',None,None,403)

def mi_error_500(request,exception=None):
    return render(request,'errores/500.html',None,None,500)