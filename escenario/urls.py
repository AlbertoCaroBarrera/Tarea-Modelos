from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos,name='lista_proyectos'),
    path("tareas/<str:texto_observacion>",views.dame_tareas_texto,name="dame_tareas_texto")
]

