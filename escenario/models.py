from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo_electronico = models.CharField(max_length=200,unique=True)
    contraseña = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(default = timezone.now)
    
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = [('Pendiente','Progreso','Completada')]
    completada = models.BooleanField()
    fecha_creacion = models.DateTimeField(default = timezone.now)
    hora_vencimiento = models.TimeField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usuarios_asignados = models.ManyToManyField(Usuario, through='Asignacion_tarea')
    

class Asignacion_tarea(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.FloatField()
    fecha_inicio = models.DateTimeField(default = timezone.now)
    fecha_fin = models.DateTimeField()
    usuario = models.ManyToManyRel(Usuario)
    creador = models.OneToOneField(Usuario,on_delete=models.CASCADE)
    

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200)
    tarea = models.ManyToManyField(Tarea)
    
class Asignacion_tarea(models.Model):
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default = timezone.now)
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default = timezone.now)
    autor = models.ManyToOneRel(Usuario,on_delete=models.CASCADE)
    tarea = models.ManyToOneRel(Tarea,on_delete=models.CASCADE)