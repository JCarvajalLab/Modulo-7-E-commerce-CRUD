from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForms
from django.contrib import messages

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
            messages.success(request,'Producto creado exitosamente')
            return redirect('lista_productos')
    else:
        form = ProductoForms()
    context = {'form': form}
    return render(request, 'productos/crear_producto.html', context)

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForms(request.POST, instance=producto )
        if form.is_valid():
            form.save()
            messages.success(request,'Producto modificado exitosamente')
            return redirect('lista_productos')
    else:
        form = ProductoForms(instance=producto)
        context = { 'form': form, 'producto': producto}
        return render(request, 'productos/editar_producto.html', context)
    
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id= id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request,'Producto eliminado exitosamente')
        return redirect('lista_productos')
    context = {'producto': producto}
    return render(request, 'productos/eliminar_producto.html', context)