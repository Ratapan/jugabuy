from django.shortcuts import render
from apps.modelo.models import Juego, perfil,Region,Ciudad
from django.contrib.auth.models import User

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

def Perfil(request, username):
    #userr = User.objects.filter(username=username)
    per = perfil.objects.get(nom_user= request.user.username)
    print(username)
    return render(request, 'modelo/perfil.html', {'perfil':per})
    #return render(request, 'modelo/perfil.html', {'user':user, 'perfil':perfil})


def Novedades(request):
    return render(request, 'modelo/novedades.html')

#def Login(request):
    #return render(request, 'modelo/login.html')


def mostrarRegiones(request):
    region = Region.objects.all()
    ciudad = Ciudad.objects.all()
    print(ciudad)
    return render(request,'modelo/crearcuenta.html',{'region':region, 'ciudad':ciudad})