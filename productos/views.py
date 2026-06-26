from django.shortcuts import render
from .models import Producto

# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    context = { 'productos': productos, }
    return render(request, 'productos/lista_productos.html', context)