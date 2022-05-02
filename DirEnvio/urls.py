'''
Created on 16 abr. 2022

@author: daniel
'''
from django.urls import path
from .import views
urlpatterns = [
    path('',views.EnvioDirecciones.as_view(), name='direccion_envio'),
    path('nueva',views.formularioDir, name='nueva direccion'),
    path('Editar/<int:pk>', views.UpdateDireccion.as_view(), name='update'),
    path('Eliminar/<int:pk>', views.DeleteDireccion.as_view(), name='remove'),
    path('default/<int:pk>', views.funcDefault, name='default'),
    ]