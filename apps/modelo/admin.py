from django.contrib import admin
from apps.modelo.models import  Region, Ciudad, Rol, perfil, Transacciones, Cesta, Juego, Compra, Key, DetalleCompra, Detalle, biblioteca, fotoPerfil
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display=  ('us_nom','us_rut','id_ciud')

admin.site.register(fotoPerfil)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Rol)
admin.site.register(perfil, UsuarioAdmin)
admin.site.register(Transacciones)
admin.site.register(Cesta)
admin.site.register(Juego)
admin.site.register(Compra)
admin.site.register(Key)
admin.site.register(Detalle)
admin.site.register(DetalleCompra)
admin.site.register(biblioteca)


