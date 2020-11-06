from django.shortcuts import render
from apps.modelo.models import Juego, perfil,Region,Ciudad
from django.contrib.auth.models import User

# Create your views here.
def Inicio(request):
    return render(request,'modelo/index.html')

def Juego(request):
    juegos = Juego.objects.all()
    return render(request, 'modelo/juegos.html',{'juego':juegos})
    
def Novedades(request):
    return render(request, 'modelo/novedades.html')


def Carrito(request):
    return render(request, 'modelo/carrito.html')

def Login(request):
    return render(request, 'modelo/login.html')

def Perfil(request):
    per = perfil.objects.get(nom_user= request.user.username)
    usu = request.user.username
    print(per.us_mail)
    return render(request, 'modelo/perfil.html', {'per':usu})

def Cuenta(request):
    return render(request, 'modelo/crearcuenta.html')






# def mostrarRegiones(request):
#     region = Region.objects.all()
#     ciudad = Ciudad.objects.all()
#     print(ciudad)
#     return render(request,'modelo/crearcuenta.html',{'region':region, 'ciudad':ciudad})