from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('registrar/', views.registrar, name='registrar'),  # Crear cuenta
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),  # Entrar
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),  # Salir
    path('dashboard/', views.dashboard, name='dashboard'),  # Panel principal
    path('cliente/crear/', views.crear_cliente, name='crear_cliente'),  # Agregar
    path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),  # Modificar
    path('cliente/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),  # Borrar
]