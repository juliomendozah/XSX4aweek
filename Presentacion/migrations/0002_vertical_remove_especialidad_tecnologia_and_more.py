# Generated by Django 4.0.2 on 2022-02-23 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Presentacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vertical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'vertical',
                'verbose_name_plural': 'verticales',
            },
        ),
        migrations.RemoveField(
            model_name='especialidad',
            name='tecnologia',
        ),
        migrations.RemoveField(
            model_name='descripcion',
            name='tecnologias',
        ),
        migrations.DeleteModel(
            name='conocimiento',
        ),
        migrations.DeleteModel(
            name='especialidad',
        ),
        migrations.AddField(
            model_name='descripcion',
            name='vertical',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Presentacion.vertical'),
            preserve_default=False,
        ),
    ]