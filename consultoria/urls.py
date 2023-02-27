# aqui guardamos las propias urls de cada aplicacion
 
from django.urls import path

# ponemos . porque las views se encuentran en la misma carpeta
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('asesoria/', views.asesoria, name='asesoria'),
    path('contacto/', views.contacto, name='contacto'),
    path('marketing/', views.marketing, name='marketing'),
    path('nosotros/', views.nosotros, name='nosotros')
]
