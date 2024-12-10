from django import forms
from .models import Cliente, Producto, Comercio

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'mail', 'comercio']
        widgets = {
            'comercio': forms.Select(attrs={'required': False}),  # Asegura que el comercio sea opcional en el formulario
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = '__all__'