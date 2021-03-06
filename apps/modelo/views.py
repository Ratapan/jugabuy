from apps.modelo.serializers import LoginSerializer
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from apps.modelo.models import Juego, perfil, Region, Ciudad, Compra, fotoPerfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages


from django.contrib import messages
# Create your views here.
from .forms import CreateUserForm, PerfilForm

from rest_framework import viewsets
from .serializers import LoginSerializer


def Inicio(request):
    return render(request, 'modelo/index.html')


def Juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'modelo/juegos.html', {'juego': juegos})


def ComprarJuego(request):

    return render(request, 'modelo/juegocomprado.html')

#	juegos = Juego.objects.all()
#	com_jue=[]
#	for i in juegos:
#		nombreDJuego = i.j_nom
#		try:
#			nom = request.POST[f'"{nombreDJuego}"']
#			com_jue.append(nom)
#			pass
#		except:
#			pass
#	jue = (f'8888888888888888888 {com_jue} 88888888888888888888888888')
#	print(f'{jue}')


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
        # formulario user
        form = CreateUserForm()
        # formulario perfil
        perfilform = PerfilForm(request.POST)
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                # messages.success(request, 'Account was created for ' + user)
                if perfilform.is_valid():
                    post = perfilform.save(commit=False)
                    post.nom_user = user
                    post.save()

                return redirect('login')

        context = {'form': form, 'perfilform': perfilform}

        return render(request, 'modelo/register.html', context)

# PERFIL


def Perfil(request):
    if perfil.objects.filter(nom_user=request.user.username).exists():
        fotos = fotoPerfil.objects.filter(nom_user=request.user.username).count()
        datosuser = perfil.objects.get(nom_user=request.user.username)
        regiones = Region.objects.all()
        comunas = Ciudad.objects.all()

        if fotos > 0:
            fotos = fotoPerfil.objects.get(nom_user=request.user.username)

        else:
            fotos = fotoPerfil.objects.filter(nom_user=request.user.username)

        data = {
            'fotos': fotos,
            'datosuser': datosuser,
            'regiones': regiones,
            'comunas': comunas
        }

        return render(request, 'modelo/datos_perfil.html', data)
    else:
  
        return redirect('actualizarperfil')
		


def biblioteca(request, user):

    juegos = Compra.objects.filter(nom_user=user)

    page = request.GET.get('page', 1)

    fotos = fotoPerfil.objects.filter(nom_user=request.user.username).count()

    try:
        paginator = Paginator(juegos, 3)
        juegos = paginator.page(page)
    except:
        raise Http404

        fotos = fotoPerfil.objects.filter(
            nom_user=request.user.username).count()

    if fotos > 0:
        fotos = fotoPerfil.objects.get(nom_user=user)
        print("+0")
        print(fotos)
    else:
        fotos = fotoPerfil.objects.filter(nom_user=user)
        print("nulo")
        print(fotos)

    data = {
        'entity': juegos,
        'paginator': paginator,
        'fotos': fotos
    }

    return render(request, 'modelo/biblioteca_perfil.html', data)


def historialperfil(request):

    juegos = Compra.objects.filter(nom_user=request.user.username)

    fotos = fotoPerfil.objects.filter(nom_user=request.user.username).count()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(juegos, 3)
        juegos = paginator.page(page)
    except:
        raise Http404

        fotos = fotoPerfil.objects.filter(
            nom_user=request.user.username).count()

    if fotos > 0:
        fotos = fotoPerfil.objects.get(nom_user=request.user.username)
        print("+0")
        print(fotos)
    else:
        fotos = fotoPerfil.objects.filter(nom_user=request.user.username)
        print("nulo")
        print(fotos)

    data = {
        'entity': juegos,
        'paginator': paginator,
        'fotos': fotos
    }

    return render(request, 'modelo/historial_perfil.html', data)


def monederoperfil(request):

    fotos = fotoPerfil.objects.filter(nom_user=request.user.username).count()

    if fotos > 0:
        fotos = fotoPerfil.objects.get(nom_user=request.user.username)
        print("+0")
        print(fotos)
    else:
        fotos = fotoPerfil.objects.filter(nom_user=request.user.username)
        print("nulo")
        print(fotos)

    data = {
        'fotos': fotos
    }

    return render(request, 'modelo/monedero_perfil.html', data)


def formcargarfoto(request):
    return render(request, 'modelo/Cambiar_foto.html')


def cargarfoto(request, user):

    nroObj = fotoPerfil.objects.filter(nom_user=request.user.username).count()

    username = user
    fot_perfil = request.FILES.get('Foto_perfil')
    fot_banner = request.FILES.get('Foto_banner')

    if nroObj > 0:

        try:
            fotoPerfil.objects.filter(nom_user=username).delete()
            fotoPerfil.objects.create(
                nom_user=username, foto_perfil=fot_perfil, foto_banner=fot_banner)
            messages.success(request, 'Fotos Actualizadas Correctamente')
            messages.success(request, "Fotos Actualizadas Correctamente")
        except:
            messages.error(request, 'Error Al actualizar las Fotos')
            

    else:

        try:
            fotoPerfil.objects.create(
                nom_user=username, foto_perfil=fot_perfil, foto_banner=fot_banner)

            messages.success(request, 'Fotos Actualizadas Correctamente')
        except:
            messages.error(request, 'Error Al actualizar las Fotos')

    return redirect('datospersonales')


def actualizardatos(request):

    # userr = perfil.objects.get(nom_user=request.user.username)

    Nom = request.POST['nombre']
    Apel = request.POST['apellido']
    # Usern = request.POST['usernme']
    Fon = request.POST['fono']
    Emai = request.POST['email']
    Direc = request.POST['direccion']

    try:
        perfil.objects.filter(nom_user=request.user.username).update(
            us_nom=Nom, us_apes=Apel, us_tel=Fon, us_dir=Direc)
        User.objects.filter(username=request.user.username).update(email=Emai)

        
        messages.success(request, "Datos Actualizados Correctamente")

    except:
        
        messages.success(request, "Error Al Actualizar los Datos")

    return redirect('datospersonales')
# ENDPERFIL

#MANTENEDOR
def mantenedor(request):
    return render(request, 'modelo/agregar_juegos.html')





def agregarJuego(request):

    nom_juego = request.POST['nombre_juego']
    descrip =  request.POST['descripcion']
    platafo = request.POST['plataforma']
    fot_juego = request.FILES.get('foto_portada')
    valor = request.POST['valor'] 
    fecha_sal = request.POST['fecha_salida']
    stock = request.POST['stock'] 
    status = request.POST['sele_status']

    try:
        Juego.objects.create(j_nom=nom_juego, j_desc=descrip, j_plt=platafo, j_port=fot_juego, j_price=valor, j_fe_sal=fecha_sal, j_stock=stock, j_status=status)
        print("======================Juegos agregado======================")
        messages.success(request, "Agregado Correctamente")
    except:
        print("======================Juegos **NO** agregado======================")
        messages.success(request, "Error, Juego No registrado")
    
    
    return redirect('mantenedor')

def listadoJuego(request):

    busqueda = request.GET.get("buscar")

    juegos = Juego.objects.all()
    print("======================================================")
    print(juegos)

    if busqueda:
        juegos = Juego.objects.filter(j_nom__icontains = busqueda)

    data = {
        'juegos': juegos
    }

    return render(request, 'modelo/listado_juego.html', data)

def cargarDatosJuego(request, id_):

    juego = Juego.objects.get(j_id=id_)

    data = {
        'juego':juego
    }

    return render(request, 'modelo/modificar_juego.html', data)

def modificarJuego(request):

    id_ = request.POST['id_juego']
    nom = request.POST['nombre_juego']
    desc = request.POST['descripcion']
    plat = request.POST['plataforma']
    #port = request.FILES.get('foto_portada') #error al actualizar
    preci = request.POST['valor']
    fech = request.POST['fecha_salida']
    stock = request.POST['stock']
    status = request.POST['sele_status']

    try:
        Juego.objects.filter(j_id=id_).update(j_nom=nom, j_desc=desc, j_plt=plat, j_price=preci, j_fe_sal=fech, j_stock=stock, j_status=status)
        print("======================Juego*Actualizado======================")
        messages.success(request, "Modificado Correctamente")
    except:
        messages.error(request, "Error, El Juego no Pudo ser Modificado")
        print("======================Juego**NO**Actualizado======================")
    
    return redirect('listadoJuego')

def eliminarJuego(request, id_):
    juego = Juego.objects.get(j_id=id_)

    try:
        juego.delete()
        messages.success(request, "Elimado Correctamente")
    except:
        messages.error(request, "Error, El Juego no Pudo ser Eliminado")
    
    return redirect('listadoJuego')


#ENDMANTENEDOR

# creando vistas para los serializadores
class LoginViewSet(viewsets.ModelViewSet):
    # se usan para enviar informacion como para recibirla
    queryset = User.objects.all()
    serializer_class = LoginSerializer


def ActualizarPerfil(request):
        perfilform = PerfilForm(request.POST)
        if request.method == 'POST':
            if perfilform.is_valid():
                user = request.user.username          
                post = perfilform.save(commit=False)
                post.nom_user = user
                post.save()

            return redirect('/')

        context = {'perfilform': perfilform}

        return render(request, 'modelo/actualizarperfil.html', context)



# def mostrarRegiones(request):
#     region = Region.objects.all()
#     ciudad = Ciudad.objects.all()
#     print(ciudad)
#     return render(request,'modelo/crearcuenta.html',{'region':region, 'ciudad':ciudad})
