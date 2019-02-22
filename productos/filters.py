from .models import Producto
import django_filters
from django import forms

class ProductoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains',label=('Código de Producto'),widget=forms.TextInput(attrs={'placeholder': ('Ingrese los 13 dígitos'),}))
    nombre = django_filters.CharFilter(lookup_expr='icontains',label=('Nombre'),widget=forms.TextInput(attrs={'placeholder': ('Ej. caños'),}))
    marca = django_filters.CharFilter(lookup_expr='icontains',label=('Marca'),widget=forms.TextInput(attrs={'placeholder': ('Ej. sigas'),}))
    class Meta:
        model = Producto
        fields = ['categoria','codigo','nombre','marca',]