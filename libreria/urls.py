from django.urls import path
from . import views

urlpatterns = [
    path('', views.ardecors, name='ardecors'),
    path('productos/', views.productos, name='productos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver-carrito/', views.ver_carrito, name='ver_carrito'),
    path('pagar/', views.pagar, name='pagar'),
    path('logout/', views.logout_view, name='logout'),
]