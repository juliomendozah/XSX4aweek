from ast import For
from django.http import HttpRequest
from django.shortcuts import redirect, render
from Presentacion.models import descripcion
from .forms import Formulario
import requests
import json
from time import localtime, strftime
# Create your views here.

def save_image(filename,file):
    print(filename)
    destination = open('/Presentacion/static/build/images/'+filename+".jpg", 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

def Presentacion(request):
    datos = descripcion.objects.all()
    return render (request,'Presentacion/presentacion_proto.html',{'datos': datos})

def agregar_voluntario(request):
    form = Formulario(request.POST,request.FILES)
    if request.method == 'POST':
    
        if form.is_valid():
            form.save()
            #save_image(request.POST['nombre'],request.FILES['foto'])
            return redirect ('/voluntarios')
    return render(request, 'Presentacion/agregar.html',{"form":form})

    
def Personal(request, CCO):
    datos = descripcion.objects.filter(CCO=CCO)
    return render(request,'Personal/base_nueva_nueva.html',{'datos': datos})

def wireless(request):
    datos = descripcion.objects.filter(vertical_id=1)
    return render(request,'Presentacion/presentacion_proto.html',{'datos': datos})

def fso(request):
    datos = descripcion.objects.filter(vertical_id=2)
    return render(request,'Presentacion/presentacion_proto.html',{'datos': datos})

def security(request):
    datos = descripcion.objects.filter(vertical_id=3)
    return render(request,'Presentacion/presentacion_proto.html',{'datos': datos})

def sp(request):
    datos = descripcion.objects.filter(vertical_id=4)
    return render(request,'Presentacion/presentacion_proto.html',{'datos': datos})

def Meraki(request):
    datos = descripcion.objects.filter(vertical_id=5)
    return render(request,'Presentacion/presentacion_proto.html',{'datos': datos})

def collab(request):
    datos = descripcion.objects.filter(vertical_id=6)
    return render(request,'Presentacion/presentacion_proto.html',{'datos': datos})

def en(request):
    datos = descripcion.objects.filter(vertical_id=8)
    return render(request,'Presentacion/presentacion_proto.html',{'datos': datos})

def Portada(request):
    return render(request,'Presentacion/portada.html')

def createwebex(request,user,CCO,man_email):

    bearer="NjQyODhiZDgtNjUxOS00MjM3LTgxMmYtYTdlYmI0OGFiMzRlYjM4MjE2MWMtNmY4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + bearer
    }

    PARTICIPANTS_LIST=[ user, CCO + '@cisco.com' , man_email]

    #Create Webex Space
    data_room = {"title": " TSX4Aweek - " + CCO + strftime('%m%d%y%H%M',localtime()) }
    req_room = requests.post("https://webexapis.com/v1/rooms", json.dumps(data_room), headers=headers).json()

    #Add participants to Webex Space
    for participant in PARTICIPANTS_LIST:
        data_participant = {"roomId": req_room["id"], "personEmail": participant}
        req_participant = requests.post("https://webexapis.com/v1/memberships", json.dumps(data_participant), headers=headers).json()

    #Send message to Webex Space
    data_msg = {"roomId": req_room["id"], "text": "Welcome to TSX4Aweek"}
    req_msg = requests.post("https://webexapis.com/v1/messages", json.dumps(data_participant), headers=headers).json()
    
    return render(request,'Presentacion/webex.html')
