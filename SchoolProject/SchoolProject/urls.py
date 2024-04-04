"""
URL configuration for SchoolProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
#from django.conf.urls import url
from StudentApp import views
#from StudentApp import views as student_views
from Usuarios import views as usuario_views


urlpatterns = [
    # Endpoint para obtener todos los estudiantes o agregar un nuevo estudiante
    path('students/', views.student_list),
    # Endpoint para obtener, actualizar o eliminar un estudiante específico
    path('students/<int:id>/', views.student_detail),
    # Endpoint para obtener estudiantes por edad
    path('students/by-edad/<int:edad>/', views.students_by_edad),  # Agregar esta línea
     # Nuevo endpoint para obtener estudiantes por rango de fechas
    path('students/by-date-range/', views.students_by_date_range),  # Agregar esta línea
    

    path('usuarios/',usuario_views.usuario_lista),
    path('usuarios/<int:id>', usuario_views.usuario_detalle),
    # Nueva ruta para validar credenciales
    path('usuarios/validar-credenciales/', usuario_views.validar_credenciales),
    #para ver contraseña en texto plano
    path('ver-contrasenia/<int:user_id>/', usuario_views.ver_contrasenia, name='ver_contrasenia'),
    path('tocken/', usuario_views.autenticar_user, name='tocken'),
    path('generar-token/', usuario_views.generar_token, name='generar-token'),
    path('decifrar/<str:token>', usuario_views.decifrar_token, name='decifrar'),

    path('admin/', admin.site.urls),
]