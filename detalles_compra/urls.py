from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_detalles_compra, name='lista_detalles_compra'),
    path('compra/<int:compra_id>/', views.lista_detalles_compra, name='lista_detalles_compra'),
    path('crear/<int:compra_id>/', views.crear_detalle_compra, name='crear_detalle_compra'),
    path('editar/<int:pk>/', views.editar_detalle_compra, name='editar_detalle_compra'),
    path('eliminar/<int:pk>/', views.eliminar_detalle_compra, name='eliminar_detalle_compra'),
    path('api/insumo/<int:insumo_id>/', views.get_insumo_info, name='get_insumo_info'),
]