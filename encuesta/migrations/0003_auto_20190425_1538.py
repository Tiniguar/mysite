# Generated by Django 2.2 on 2019-04-25 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0002_auto_20190425_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='Pregunta_Nombre',
            new_name='pregunta_Nombre',
        ),
        migrations.RenameField(
            model_name='seleccion',
            old_name='Pregunta',
            new_name='pregunta',
        ),
        migrations.RenameField(
            model_name='seleccion',
            old_name='Seleccion_Nombre',
            new_name='seleccion_Nombre',
        ),
    ]
