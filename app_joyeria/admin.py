from django.contrib import admin
from .models import Proveedor, Producto, Venta

# Registrar los modelos aquí.

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)