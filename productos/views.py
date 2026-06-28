from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForms

# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    context = { 'productos': productos, }
    return render(request, 'productos/lista_productos.html', context)

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForms()
    context = {'form': form}
    return render(request, 'productos/crear_producto.html', context)