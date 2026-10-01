from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de Django
    path('', include('ventas_app.urls')),  # Nuestras páginas
]