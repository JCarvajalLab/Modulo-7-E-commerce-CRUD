from django import forms
from .models import Producto

class ProductoForms(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['nombre','descripcion', 'precio','stock', 'categoria',]