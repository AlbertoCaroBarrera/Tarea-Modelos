# Generated by Django 3.2.22 on 2023-10-25 12:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion_tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField()),
                ('fecha_asignacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo_electronico', models.CharField(max_length=200, unique=True)),
                ('contraseña', models.CharField(max_length=200)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('prioridad', models.IntegerField()),
                ('completada', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora_vencimiento', models.TimeField()),
                ('creador_tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador_tarea', to='escenario.usuario')),
                ('usuarios_asignados', models.ManyToManyField(related_name='usuarios_asignados', through='escenario.Asignacion_tarea', to='escenario.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('duracion', models.FloatField()),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_fin', models.DateTimeField()),
                ('creador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='escenario.usuario')),
                ('tareas', models.ManyToManyField(to='escenario.Tarea')),
                ('usuario', models.ManyToManyField(related_name='usuario', to='escenario.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('tarea', models.ManyToManyField(to='escenario.Tarea')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_comentario', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.usuario')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.tarea')),
            ],
        ),
        migrations.AddField(
            model_name='asignacion_tarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.tarea'),
        ),
        migrations.AddField(
            model_name='asignacion_tarea',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.usuario'),
        ),
    ]
