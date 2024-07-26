from django.contrib import admin
from .models import Producto, Contacto, OrdenCompra, DetalleCompra, DetalleVenta, Venta, Proveedor, Carrito, ItemCarrito

# Registra tus modelos aquí
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(OrdenCompra)
admin.site.register(DetalleCompra)
admin.site.register(DetalleVenta)
admin.site.register(Venta)
admin.site.register(Proveedor)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)