from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Producto, Comercio
from .forms import ClienteForm, ProductoForm, ComercioForm
from django.shortcuts import render

def inicio(request):
    return render(request, "app_coder/index.html")


# Vistas para Producto
def lista_productos(request):
    query = request.GET.get('q', '')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    
    return render(request, 'app_coder/productos.html', {'productos': productos})

def producto_formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'app_coder/forms/producto-formulario.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app_coder/editar-producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'app_coder/confirmar_eliminacionproducto.html', {'producto': producto})

def detalle_producto_view(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, "app_coder/detalle-producto.html", {"producto": producto})

# Vistas similares para Comercio
def lista_comercios(request):
    comercios = Comercio.objects.all()
    return render(request, 'app_coder/comercios.html', {'comercios': comercios})

def comercio_formulario(request):
    if request.method == 'POST':
        form = ComercioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comercios')
    else:
        form = ComercioForm()
    return render(request, 'app_coder/forms/comercio-formulario.html', {'form': form})


def editar_comercio(request, pk):
    comercio = get_object_or_404(Comercio, pk=pk)
    if request.method == 'POST':
        form = ComercioForm(request.POST, instance=comercio)
        if form.is_valid():
            form.save()
            return redirect('comercios')
    else:
        form = ComercioForm(instance=comercio)
    return render(request, 'app_coder/editar-comercio.html', {'form': form})

def eliminar_comercio(request, pk):
    comercio = get_object_or_404(Comercio, pk=pk)
    if request.method == 'POST':
        comercio.delete()
        return redirect('comercios')
    return render(request, 'app_coder/confirmar_eliminacioncomercio.html', {'comercio': comercio})

# Vistas similares para Cliente
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_coder/clientes.html', {'clientes': clientes})

def cliente_formulario(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'app_coder/forms/cliente-formulario.html', {'form': form})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'app_coder/editar-cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'app_coder/confirmar_eliminacion.html', {'cliente': cliente})