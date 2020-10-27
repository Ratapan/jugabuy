from django.shortcuts import render
from apps.modelo.models import Juego
# Create your views here.
def Inicio(request):
    return render(request,'modelo/index.html')

def Cuenta(request):
    return render(request, 'modelo/crearcuenta.html')

def Carrito(request):
    return render(request, 'modelo/carrito.html')

def Juego_v(request):
    juegos = Juego.objects.all()
    return render(request, 'modelo/juegos.html',{'juego':juegos})

def Perfil(request):
    return render(request, 'modelo/perfil.html')

def Novedades(request):
    return render(request, 'modelo/novedades.html')