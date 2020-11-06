from django.contrib import admin
from django.urls import path, include
from .views import Inicio,Carrito,Juego_v,Perfil,Novedades,mostrarRegiones
#from .import views
from django.contrib.auth.views import LoginView,LogoutView
#Primera urls para vistas con el alias

urlpatterns=[
    path('', Inicio, name="Inicio"),
    #path('CrearCuenta', Cuenta, name="Cuenta"),
    path('carrito', Carrito, name="Carrito"),
    path('Juegos', Juego_v, name="juego"),
    
    path('perfil/<str:username>/', Perfil, name="perfil"),
    path('novedades', Novedades, name="novedades"),
    path('login', LoginView.as_view(template_name='modelo/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='modelo/index.html'), name="logout"),

    path('crearcuenta.html/',mostrarRegiones ,name="mostrarregiones"),  
]