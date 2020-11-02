from django.shortcuts import render
from apps.modelo.models import Juego,Usuario,Region,Ciudad

from rest_framework.decorators import api_view
from django.http import JsonResponse,Http404,HttpResponse
from rest_framework.response import Response
from apps.modelo.serializers import UsuarioSerializer
from rest_framework import status

# Create your views here.
def Inicio(request):
    return render(request,'modelo/index.html')

# def Cuenta(request):
#     return render(request, 'modelo/crearcuenta.html')

def Carrito(request):
    return render(request, 'modelo/carrito.html')

def Juego_v(request):
    juegos = Juego.objects.all()
    return render(request, 'modelo/juegos.html',{'juego':juegos})

def Perfil(request):
    return render(request, 'modelo/perfil.html')

def Novedades(request):
    return render(request, 'modelo/novedades.html')


# def mostrarRegiones(request):
#     region = Region.objects.all()
#     print(region)
#     return render(request,'modelo/crearcuenta.html',{'region':region})

def mostrarRegiones(request):
    region = Region.objects.all()
    ciudad = Ciudad.objects.all()
    print(region)
    return render(request,'modelo/crearcuenta.html',{'region':region, 'ciudad':ciudad})


@api_view(['GET'])
def GetUser(request):

    try:
        result = Usuario.objects.all()
       
    except Usuario.DoesNotExist:
        raise Http404("User does not exist")

    print(result)
    return render(request, 'modelo/index.html',{'boby':result})



@api_view(['POST'])
def login(request):
    # AQUI SE OBTIENE LA DATA DEL BODY
    username = request.data['username'] 
    print(username)
    # COMPARO EL EMAIL CON EL EMAIL DE LA BD
    user= Usuario.objects.get(us_mail=username)

    # COMPARANDO PASS CON LA PASS DE LA DB
    if user.us_contr == request.data['password']:
        return JsonResponse({'ok': username})
        # return render(request, 'modelo/perfil.html')
    else:
        return JsonResponse({'false': username})