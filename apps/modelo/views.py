from django.shortcuts import render, redirect
from apps.modelo.models import Juego, perfil,Region,Ciudad
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
# Create your views here.
from .forms import CreateUserForm

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

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('Inicio')
			

		context = {'form':form}
		return render(request, 'modelo/register.html', context)





# def mostrarRegiones(request):
#     region = Region.objects.all()
#     ciudad = Ciudad.objects.all()
#     print(ciudad)
#     return render(request,'modelo/crearcuenta.html',{'region':region, 'ciudad':ciudad})