from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

# Primera urls para vistas con el alias

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('CrearCuenta', views.Cuenta, name="cuenta"),
    path('carrito', views.Carrito, name="carrito"),
    path('Juegos', views.Juegos, name="juego"),

   # path('perfil', views.Perfil, name="perfil"),
    path('novedades', views.Novedades, name="novedades"),
    path('login', LoginView.as_view(
        template_name='modelo/login.html'), name="login"),
    path('logout', LogoutView.as_view(
        template_name='modelo/index.html'), name="logout"),
    path('register/', views.registerPage, name="register"),
    #     path('crearcuenta.html/',mostrarRegiones ,name="mostrarregiones"),
    
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='modelo/password_reset.html',
             subject_template_name='modelo/password_reset_subject.txt',
             email_template_name='modelo/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='modelo/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='modelo/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='modelo/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    #PERFIL
    path('perfil/datos-personales/', views.Perfil, name="datospersonales"),
    path('perfil/biblioteca/<user>/', views.biblioteca, name="biblioteca"),
    path('perfil/historial/', views.historialperfil, name="historialperfil"),
    path('perfil/mondero/', views.monederoperfil, name="monederoperfil"),
    path('perfil/actualizar-fotos', views.formcargarfoto, name="cargarfoto"),
    path('perfil/cargarfoto/<user>/', views.cargarfoto, name="cargarfoto"),
    #ENDPERFIL



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)