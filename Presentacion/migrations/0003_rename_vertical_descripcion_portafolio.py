# Generated by Django 4.0.2 on 2022-02-23 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Presentacion', '0002_vertical_remove_especialidad_tecnologia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='descripcion',
            old_name='vertical',
            new_name='portafolio',
        ),
    ]
