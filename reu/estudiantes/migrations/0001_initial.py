# Generated by Django 4.2.2 on 2023-06-23 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('nombre_carrera', models.CharField(max_length=50)),
                ('duracion', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1, null=True)),
                ('email', models.CharField(max_length=50)),
                ('vigencia', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50)),
                ('fecha_matricula', models.DateField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.estudiante')),
            ],
        ),
    ]
