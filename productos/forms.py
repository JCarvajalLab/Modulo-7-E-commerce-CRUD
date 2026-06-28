from django import forms
from .models import Producto

class ProductoForms(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['nombre','descripcion', 'precio','stock', 'categoria',]

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if not nombre:
            raise forms.ValidationError('El nombre no puede estar vacio.')
        return nombre
    
    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a 0')
        return precio
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo')
        return stock