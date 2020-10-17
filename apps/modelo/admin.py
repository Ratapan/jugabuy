from django.contrib import admin
from apps.modelo.models import  Region, Ciudad, Rol, Usuario, Transacciones, Cesta, Juego, Compra, Key, DetalleCompra, Detalle, biblioteca
# Register your models here.

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Transacciones)
admin.site.register(Cesta)
admin.site.register(Juego)
admin.site.register(Compra)
admin.site.register(Key)
admin.site.register(Detalle)
admin.site.register(DetalleCompra)
admin.site.register(biblioteca)