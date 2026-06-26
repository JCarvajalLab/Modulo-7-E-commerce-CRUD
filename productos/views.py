from django.shortcuts import render

# Create your views here.

def lista_productos(request):
    return render(request, 'productos/lista_productos.html')