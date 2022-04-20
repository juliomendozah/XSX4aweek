from django import forms
from django.forms.models import ModelForm
from .models import descripcion

class Formulario(forms.ModelForm):

    class Meta : 
        model = descripcion
        fields = ('nombre','puesto','CCO','manager','man_email','descripcion','ubicacion','vertical','foto','idioma','requerimientos','soluciones')
        



    

