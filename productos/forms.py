from django import forms
from productos.models import Producto, Categoria
from django.core.validators import RegexValidator
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class CategoriaForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    nombre = forms.CharField(
        validators=[RegexValidator(r'^[a-zA-Z0-9/ñÑáéíóúÁÉÍÓÚ\s]{1,50}$', "Ingrese nombre válido")])

    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

        """def __init__(self, *args, **kwargs):
            super(CategoriaForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                        'class': 'form-control'
                    })"""


class ProductoForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    codigo = forms.CharField(label=('Código de Producto'),
        validators=[RegexValidator(r'^[0-9]{13}$', "Ingrese un código válido de 13 dígitos (Sólo números. Ej. 1234567891157)")])
    
    nombre = forms.CharField(
        validators=[RegexValidator(r'^[a-zA-Z0-9/ñÑáéíóúÁÉÍÓÚ\s]{1,50}$', "Ingrese nombre válido")])

    marca = forms.CharField(
        validators=[RegexValidator(r'^[a-zA-Z0-9/ñÑáéíóúÁÉÍÓÚ\s]{1,50}$', "Ingrese una marca válida")])

    precio = forms.DecimalField(max_digits=8, decimal_places=2, min_value=0)

    stock = forms.IntegerField(min_value=0, required=True)

    class Meta:
        model = Producto
        fields = ['codigo','categoria','nombre', 'marca', 'tipo_producto', 'precio', 'stock','imagenes']

        """def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                        'class': 'form-control'
                    })"""

