from django.shortcuts import render, redirect, get_object_or_404
from apps.modelo.models import Juego, perfil,Region,Ciudad, Compra
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import Http404

from django.contrib import messages
# Create your views here.
from .forms import CreateUserForm, PerfilForm

def Inicio(request):
    return render(request,'modelo/index.html')

def Juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'modelo/juegos.html',{'juego':juegos})
    
def Novedades(request):
    return render(request, 'modelo/novedades.html')


def Carrito(request):
    return render(request, 'modelo/carrito.html')

def Login(request):
    return render(request, 'modelo/login.html')



def Cuenta(request):
    return render(request, 'modelo/crearcuenta.html')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('Inicio')
	else:
		#formulario user
		form = CreateUserForm()
		#formulario perfil
		perfilform = PerfilForm(request.POST)
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				if perfilform.is_valid():
    					post = perfilform.save(commit=False)
    					post.nom_user=user
    					post.save()
    					

				return redirect('Inicio')
			

		context = {'form':form,'perfilform':perfilform}

		return render(request, 'modelo/register.html', context)

#PERFIL
def Perfil(request):
    per = perfil.objects.get(nom_user= request.user.username)
    usu = request.user.username
	

    return render(request, 'modelo/datos_perfil.html', {'per':usu})

def biblioteca(request, user):

	juegos = Compra.objects.filter(nom_user=user)
	
	page = request.GET.get('page', 1)


	try:
		paginator = Paginator(juegos, 3)
		juegos = paginator.page(page)
	except:
		raise Http404

	data = {
		'entity':juegos,
		'paginator':paginator
	}

	return render(request, 'modelo/biblioteca_perfil.html', data)

def historialperfil(request):
	return render(request, 'modelo/historial_perfil.html')

def monederoperfil(request):
	return render(request, 'modelo/monedero_perfil.html')


#ENDPERFIL





# def mostrarRegiones(request):
#     region = Region.objects.all()
#     ciudad = Ciudad.objects.all()
#     print(ciudad)
#     return render(request,'modelo/crearcuenta.html',{'region':region, 'ciudad':ciudad})