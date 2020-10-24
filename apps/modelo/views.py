from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,'modelo/index.html')

def Cuenta(request):
    return render(request, 'modelo/crearcuenta.html')

def Carrito(request):
    return render(request, 'modelo/carrito.html')

def Juego(request):
    return render(request, 'modelo/juegos.html')

def Perfil(request):
    return render(request, 'modelo/perfil.html')

def Novedades(request):
    return render(request, 'modelo/novedades.html')