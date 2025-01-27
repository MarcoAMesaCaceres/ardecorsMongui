from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from articles.models import Article

from django.http import HttpResponse, Http404
import os
from datetime import datetime
from django.conf import settings
import subprocess
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

def ardecors(request):
    return render(request, 'ardecors.html')

def productos(request):

    return render(request, 'productos.html', {'productos': productos})

def sobre(request):
    return render(request, 'sobre.html')

def contacto(request):
    return render(request, 'contacto.html', {'contato': contacto})


@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
def crear_articles(request):
    return render(request, 'crear_articles.html')
def lista_articles(request):
    return render(request, 'lista_articles.html')
def editar_articles(request):
    return render(request, 'editar_articles.html')
def eliminar_articles(request):
    return render(request, 'eliminar_articles.html')
def base_articles(request):
    return render(request, 'base_articles.html')

def base_tareas(request):
    return render(request, 'base_tareas.html')
def crear_tareas(request):
    return render(request, 'crear_tareas.html')
def lista_tareas(request):
    return render(request, 'lista_tareas.html')
def editar_tareas(request):
    return render(request, 'editar_tareas.html')
def eliminar_tareas(request):
    return render(request, 'eliminar_tareas.html')

def base_compras(request):
    return render(request, 'base_compras.html')
def crear_compras(request):
    return render(request, 'crear_compras.html')
def lista_compras(request):
    return render(request, 'lista_compras.html')
def editar_compras(request):
    return render(request, 'editar_compras.html')
def eliminar_compras(request):
    return render(request, 'eliminar_compras.html')

def base_detalle_compra(request):
    return render(request, 'base_detalle_compra.html')
def crear_detalle_compra(request):
    return render(request, 'crear_detalle_compra.html')
def lista_detalles_compra(request):
    return render(request, 'lista_detalles_compra.html')
def editar_detalle_compra(request):
    return render(request, 'editar_detalles_compra.html')
def eliminar_detalle_compra(request):
    return render(request, 'eliminar_detalle_compra.html')
def lista_ayuda(request):
    return render(request, 'lista_ayuda.html')
def detalle_ayuda(request):
    return render(request, 'detalle_ayuda.html')
def base_ayuda(request):
    return render(request, 'base_ayuda.html')


def base_venta(request):
    return render(request, 'base_venta.html')
def crear_venta(request):
    return render(request, 'crear_venta.html')
def lista_ventas(request):
    return render(request, 'lista_ventas.html')
def editar_venta(request):
    return render(request, 'editar_venta.html')
def eliminar_venta(request):
    return render(request, 'eliminar_venta.html')

def base_detalle_venta(request):
    return render(request, 'base_detalle_venta.html')
def crear_detalle_venta(request):
    return render(request, 'crear_detalle_venta.html')
def lista_detalles_venta(request):
    return render(request, 'lista_detalles_venta.html')
def editar_detalle_venta(request):
    return render(request, 'editar_detalle_venta.html')
def eliminar_detalle_venta(request):
    return render(request, 'eliminar_detalle_venta.html')

def base_proveedor(request):
    return render(request, 'base_proveedor.html')
def crear_proveedor(request):
    return render(request, 'crear_proveedor.html')
def lista_proveedores(request):
    return render(request, 'lista_proveedores.html')
def editar_proveedor(request):
    return render(request, 'editar_proveedor.html')
def eliminar_proveedor(request):
    return render(request, 'eliminar_proveedor.html')

def login(request):
    return render(request, 'login.html')
def user_edit(request):
    return render(request, 'user_edit.html')
def user_delete(request):
    return render(request, 'user_delete.html')
def user_list(request):
    return render(request, 'user_list.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')


def password_reset_email(request):
    return render(request, 'password_reset_email.html')
def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')
def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')
def password_reset_done(request):
    return render(request, 'password_reset_done.html')
def password_reset(request):
    return render(request, 'password_reset.html')
def base_usuario(request):
    return render(request, 'base_usuario.html')

def base_clientes(request):
    return render(request, 'base_clientes.html')
def crear_clientes(request):
    return render(request, 'crear_clientes.html')
def lista_clientes(request):
    return render(request, 'lista_clientes.html')
def editar_clientes(request):
    return render(request, 'editar_clientes.html')
def eliminar_clientes(request):
    return render(request, 'eliminar_clientes.html')

def logout_view(request):
    logout(request)
    return redirect('ardecors')


def backup_databases(request):
    return render(request, 'backup_databases.html')



def backup_database(request):
    try:
        # Obtener la configuración de la base de datos
        db_settings = settings.DATABASES['default']
        db_name = db_settings['NAME']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_host = db_settings['HOST']
        db_port = db_settings['PORT']

        # Crear el nombre del archivo de respaldo
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"backup_{timestamp}.sql"
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        backup_path = os.path.join(backup_dir, filename)

        # Asegurarse de que el directorio de respaldos existe
        os.makedirs(backup_dir, exist_ok=True)

        # Comando para crear el respaldo
        command = (
            f"mysqldump -h {db_host} -P {db_port} -u {db_user} -p{db_password} "
            f"{db_name} > {backup_path}"
        )

        # Ejecutar el comando
        subprocess.run(command, shell=True, check=True)

        messages.success(request, f"Respaldo creado exitosamente: {filename}")
    except Exception as e:
        messages.error(request, f"Error al crear el respaldo: {str(e)}")

    return redirect('backup_list')


def backup_list(request):
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    backups = []
    for filename in os.listdir(backup_dir):
        if filename.endswith('.sql'):
            file_path = os.path.join(backup_dir, filename)
            created_at = datetime.fromtimestamp(os.path.getctime(file_path))
            size = os.path.getsize(file_path)
            backups.append({
                'filename': filename,
                'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'size': f"{size / 1024 / 1024:.2f} MB"
            })
    
    backups.sort(key=lambda x: x['created_at'], reverse=True)
    
    # Paginación
    paginator = Paginator(backups, 10)  # 10 respaldos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'backup_list.html', {'page_obj': page_obj})


def delete_backup(request, filename):
    if request.method == 'POST':
        file_path = os.path.join(settings.BASE_DIR, 'backups', filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            messages.success(request, f"Respaldo {filename} eliminado exitosamente")
        else:
            messages.error(request, f"El archivo {filename} no existe")
    return redirect('backup_list')


def delete_backup(request, filename):
    if request.method == 'POST':
        file_path = os.path.join(settings.BASE_DIR, 'backups', filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            messages.success(request, f"Respaldo {filename} eliminado exitosamente")
        else:
            messages.error(request, f"El archivo {filename} no existe")
    return redirect('backup_list')


def restore_database(request):
    if request.method == 'GET':
        file = request.GET.get('file')
        if file:
            try:
                # Obtener la configuración de la base de datos
                db_settings = settings.DATABASES['default']
                db_name = db_settings['NAME']
                db_user = db_settings['USER']
                db_password = db_settings['PASSWORD']
                db_host = db_settings['HOST']
                db_port = db_settings['PORT']

                backup_dir = os.path.join(settings.BASE_DIR, 'backups')
                backup_path = os.path.join(backup_dir, file)

                if not os.path.exists(backup_path):
                    raise FileNotFoundError(f"El archivo de respaldo {file} no existe")

                # Comando para restaurar la base de datos
                command = (
                    f"mysql -h {db_host} -P {db_port} -u {db_user} -p{db_password} "
                    f"{db_name} < {backup_path}"
                )

                # Ejecutar el comando
                subprocess.run(command, shell=True, check=True)

                messages.success(request, f"Base de datos restaurada desde {file}")
            except Exception as e:
                messages.error(request, f"Error al restaurar la base de datos: {str(e)}")
        else:
            messages.error(request, "No se especificó un archivo para restaurar")
    
    return redirect('backup_list')

def download_backup(request, filename):
    file_path = os.path.join(settings.BASE_DIR, 'backups', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


from django.shortcuts import render
from articles.models import Article

def productos(request):
    # Obtiene todos los artículos de la base de datos
    articles = Article.objects.all()
    # Pasa los artículos al template de productos
    return render(request, 'productos.html', {'articles': articles})