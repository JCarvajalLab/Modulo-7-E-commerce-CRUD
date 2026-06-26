from django.contrib import admin
from.models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'categoria',
        'precio',
        'stock',
        'creado_en',)
    search_fields = (
        'nombre',
        'descripcion',
    )
    list_filter = (
        "categoria",
    )
    ordering = (
        "nombre",
    )