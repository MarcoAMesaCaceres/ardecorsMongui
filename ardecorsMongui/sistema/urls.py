"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libreria/', include('libreria.urls')),
    path('tareas/', include('tareas.urls')),
    path('articles/', include('articles.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('compras/', include('compras.urls')),
    path('detalles_compra/', include('detalles_compra.urls')),
    path('detalles_venta/', include('detalles_venta.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('ventas/', include('ventas.urls')),
    path('ayuda/', include('ayuda.urls')),
    path('clientes/', include('clientes.urls')),
    path('insumos/', include('insumos.urls')),
    
    # Añade esta línea para redirigir la raíz a la página principal de 'libreria'
    path('', RedirectView.as_view(url='/libreria/', permanent=True)),
]

# Añade esta condición para servir archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Configuración para archivos de medios
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)