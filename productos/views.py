# -*- coding: utf-8 -*-
from .render import Render
from django.utils import timezone
from django.http import HttpResponse
from django.conf import settings
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django_filters.views import BaseFilterView
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from usuarios.models import UserProfile
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from .filters import ProductoFilter



@method_decorator(login_required, name='dispatch')
class HomeInventario(generic.ListView):
    model = Producto
    template_name = 'inventario.html'

    def get_context_data(self, **kwargs):
        productos = Producto.objects.all().count()
        categorias = Categoria.objects.all().count()
        usuarios = UserProfile.objects.all().count()
        context = super(HomeInventario, self).get_context_data(**kwargs)
        context.update({'produ': productos, 'categ': categorias, 'usuarios': usuarios})
        return context


@method_decorator(login_required, name='dispatch')
class ListadoProductos(generic.ListView):
    model = Producto
    template_name = 'listado_productos.html'
    context_object_name = 'productos'


@method_decorator(login_required, name='dispatch')
class CrearProducto(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'create_producto.html'
    form_class = ProductoForm
    success_message = 'Producto creado con éxito...'
    success_url = reverse_lazy('productos:listado_productos')


@method_decorator(login_required, name='dispatch')
class ModificarProducto(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Producto
    template_name = 'update_producto.html'
    form_class = ProductoForm
    success_message = 'Producto actualizado con éxito...'
    success_url = reverse_lazy('productos:listado_productos')


@method_decorator(login_required, name='dispatch')
class DetalleProducto(generic.DetailView):
    model = Producto
    template_name = 'read_producto.html'


@method_decorator(login_required, name='dispatch')
class EliminarProducto(DeleteAjaxMixin, generic.DeleteView):
    model = Producto
    template_name = 'delete_producto.html'
    success_message = 'Producto eliminado con éxito...'
    success_url = reverse_lazy('productos:listado_productos')


class Productos(BaseFilterView, generic.ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'
    filterset_class = ProductoFilter
    paginate_by = 6

class ProductoDetalle(generic.DetailView):
    model = Producto
    template_name = 'detalle_producto.html'

# --------------  Categorias  --------------------- # 

@method_decorator(login_required, name='dispatch')
class ListadoCategorias(generic.ListView):
    model = Categoria
    template_name = 'listado_categorias.html'
    context_object_name = 'categorias'


@method_decorator(login_required, name='dispatch')
class CrearCategoria(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'create_categoria.html'
    form_class = CategoriaForm
    success_message = 'Categoría creada con éxito...'
    success_url = reverse_lazy('productos:listado_categorias')


@method_decorator(login_required, name='dispatch')
class ModificarCategoria(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Categoria
    template_name = 'update_categoria.html'
    form_class = CategoriaForm
    success_message = 'Categoría actualizada con éxito...'
    success_url = reverse_lazy('productos:listado_categorias')


@method_decorator(login_required, name='dispatch')
class DetalleCategoria(generic.DetailView):
    model = Categoria
    template_name = 'read_categoria.html'


@method_decorator(login_required, name='dispatch')
class EliminarCategoria(DeleteAjaxMixin, generic.DeleteView):
    model = Categoria
    template_name = 'delete_categoria.html'
    success_message = 'Categoría eliminada con éxito...'
    success_url = reverse_lazy('productos:listado_categorias')


class Pdf(generic.View):
    def get(self, request):
        categoria = Categoria.objects.all()#.order_by('nombre')
        fecha = timezone.now()
        context = {
            'fecha': fecha,
            'categoria': categoria,
            'request': request
        }
        print(categoria)
        return Render.render('reporte_categoria.html', context)