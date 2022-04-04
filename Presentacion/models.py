from distutils.command.upload import upload
from tkinter import VERTICAL
from django.db.models.deletion import CASCADE
from django.db import models
from multiselectfield import MultiSelectField

opciones_tecnologias = (
    ('Thousand Eyes','Thousand Eyes'),
    ('Intersight','Intersight'),
    ('AppDynamics','AppDynamics'),
    ('Webex','Webex'),
    ('Umbrella','Umbrella'),
    ('SD-WAN','SD-WAN'),
    ('SASE','SASE'),
    ('APIC','APIC'),
    ('IoT','IoT')
)

idiomas = (
    ('Spanish','Spanish'),
    ('English','English'),
    ('Portuguese','Portuguese')
    )

class rol(models.Model):
    posicion = models.CharField(max_length=20)

    class Meta:
        verbose_name = "rol"
        verbose_name_plural = "roles"

    def __str__(self):
        return self.posicion
        
class area(models.Model):
    region = models.CharField(max_length=20)

    class Meta:
        verbose_name = "area"
        verbose_name_plural = "areas"

    def __str__(self):
        return self.region


class portafolio (models.Model):
    area = models.CharField(max_length=20)

    class Meta:
        verbose_name = "vertical"
        verbose_name_plural = "verticales"

    def __str__(self):
        return self.area

class lengua(models.Model):
    lengua = models.CharField(max_length=20)

    class Meta:
        verbose_name = "lengua"
        verbose_name_plural = "lenguas"

    def __str__(self):
        return self.lengua

class descripcion(models.Model):
    nombre = models.CharField(max_length=50)
    puesto = models.ForeignKey(rol,on_delete=CASCADE)
    CCO = models.CharField(max_length=10)
    manager = models.CharField(max_length=50)
    man_email = models.EmailField()
    ubicacion = models.ForeignKey(area,on_delete=CASCADE)
    vertical= models.ForeignKey(portafolio,on_delete=CASCADE)
    foto = models.ImageField(upload_to = 'media/Imagenes')
    idioma = MultiSelectField(choices=idiomas)
    requerimientos = models.IntegerField()
    soluciones = MultiSelectField(choices=opciones_tecnologias)


    

