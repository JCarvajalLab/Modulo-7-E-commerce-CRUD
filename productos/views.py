from django.shortcuts import render
from .models import Producto
from .forms import ProductoForms

# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    context = { 'productos': productos, }
    return render(request, 'productos/lista_productos.html', context)

def crear_producto(request):
    form = ProductoForms()
    context = {'form': form}
    return render(request, 'productos/crear_producto.html', context)