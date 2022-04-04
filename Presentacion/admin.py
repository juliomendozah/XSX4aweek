from django.contrib import admin
from Presentacion.models import *

# Register your models here.


class Descripcion_Admin(admin.ModelAdmin):
    list_display = ('nombre','puesto','CCO','manager','man_email','ubicacion','vertical','requerimientos')


admin.site.register(descripcion,Descripcion_Admin)
admin.site.register(rol)
admin.site.register(area)
#admin.site.register(conocimiento)
admin.site.register(portafolio)
admin.site.register(lengua)
