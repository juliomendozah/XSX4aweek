from unicodedata import name
from django.urls import path, re_path
from Presentacion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('voluntarios/',views.Presentacion, name= 'Presentacion'),
    re_path(r'^presentar/(?P<CCO>\w+)$',views.Personal,name= 'Personal'),
    path('agregar/',views.agregar_voluntario,name='Agregar'),
    path('meraki/',views.Meraki,name='Meraki'),
    path('fso/',views.fso,name='FSO'),
    path('en/',views.en,name='EN'), #Enterprise Networking
    path('wireless/',views.wireless,name='Wireless'),
    path('security/',views.security,name='Security'),
    path('collab/',views.collab,name='Collab'),
    path('sp/',views.sp,name='SP'),
    path('', views.Portada,name = 'Portada'),
    path('webex/<str:user>/<str:CCO>/<str:man_email>/',views.createwebex,name= 'webex')
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)