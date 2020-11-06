from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib.auth.views import LoginView,LogoutView
#Primera urls para vistas con el alias

urlpatterns=[
    path('', views.Inicio, name="Inicio"),
    path('CrearCuenta', views.Cuenta, name="cuenta"),
    path('carrito', views.Carrito, name="carrito"),
    path('Juegos', views.Juego, name="juego"),
    
    path('perfil', views.Perfil, name="perfil"),
    path('novedades', views.Novedades, name="novedades"),
    path('login', LoginView.as_view(template_name='modelo/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='modelo/index.html'), name="logout"),
    path('register/', views.registerPage, name="register"),
#     path('crearcuenta.html/',mostrarRegiones ,name="mostrarregiones"),  
    ]