# Generated by Django 3.2.8 on 2022-04-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presentacion', '0011_alter_descripcion_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descripcion',
            name='foto',
            field=models.ImageField(upload_to='Presentacionb/static/build/images'),
        ),
    ]
