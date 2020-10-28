from django.contrib import admin
from django.urls import path, include
from .views import Inicio,Cuenta,Carrito,Juego_v,Perfil,Novedades
from .import views

#Primera urls para vistas con el alias

urlpatterns=[
    path('', Inicio, name="Inicio"),
    path('CrearCuenta', Cuenta, name="Cuenta"),
    path('carrito', Carrito, name="Carrito"),
    path('Juegos', Juego_v, name="juego"),
    path('Perfil', Perfil, name="perfil"),
    path('novedades', Novedades, name="novedades"),
    

]