from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Producto, Venta
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Página principal
def index(request):
    return render(request, 'index.html')


# Registro de usuario
def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})


# Iniciar sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {'form': form})


# Cerrar sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('index')


# Panel principal — solo si estás conectado
@login_required
def dashboard(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    ventas = Venta.objects.all()
    return render(request, 'dashboard.html', {
        'clientes': clientes,
        'productos': productos,
        'ventas': ventas
    })


# Crear cliente
@login_required
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        Cliente.objects.create(nombre=nombre, apellido=apellido, telefono=telefono)
        return redirect('dashboard')
    return render(request, 'crear_cliente.html')


# Editar cliente
@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.save()
        return redirect('dashboard')
    return render(request, 'editar_cliente.html', {'cliente': cliente})


# Eliminar cliente
@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('dashboard')
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})