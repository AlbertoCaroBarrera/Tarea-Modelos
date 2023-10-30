from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos,name='lista_proyectos'),
    path('tareas/<int:id_proyecto>',views.tareas,name="tareas"),
    path('usuarios/<int:id_tarea>',views.usuarios,name = "usuarios"),
    path('tareas-con-observaciones/<str:texto>',views.tareas_con_observaciones,name='tareas_con_observaciones'),
    path('tareas-completadas-entre-años/<int:fecha1>/<int:fecha2>',views.tareas_completadas_entre_años,name='tareas_completadas_entre_años'),
    path('ultimo-usuario-comentado/<int:id_tarea>',views.ultimo_usuario_comentado,name="ultimo_usuario_comentado"),
    path('comentario-comienza-palabra-anyo/<str:texto>/<int:anyo>',views.comentario_comienza_palabra_anyo,name="comentario_comienza_palabra_anyo"),
    path('etiquetas-tareas-proyecto/<int:id_proyecto>',views.etiquetas_tareas_proyecto,name="etiquetas_tareas_proyecto"),
    path('usuarios-sin-tarea/<int:tarea_id>',views.usuarios_sin_tarea,name="usuarios_sin_tarea"),
]


