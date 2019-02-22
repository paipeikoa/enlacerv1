from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

    def get_producto_count(self):
        return Producto.objects.filter(categoria_id=self).count()

class Producto(models.Model):
    codigo = models.CharField(blank=True, null=True, max_length=13, unique=True) 
    categoria = models.ForeignKey(
                Categoria, on_delete=models.CASCADE,
                null=True, verbose_name='Categoria', related_name='+')
    KILOS = 1
    METROS = 2
    UNIDADES = 3
    LITROS = 4
    TIPO_DE_PRODUCTO = (
        (KILOS, 'Kilogramos'),
        (METROS, 'Metros'),
        (UNIDADES, 'Unidad'),
        (LITROS, 'Litros'),
    )
    nombre = models.CharField(max_length=50, null=True)
    marca = models.CharField(max_length=50)
    tipo_producto = models.PositiveSmallIntegerField(
                    choices=TIPO_DE_PRODUCTO, blank=True,
                    null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    stock = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    imagenes = models.ImageField(upload_to='images/', null=True, default='images/producto-sin-imagen.jpg')

    def __str__(self):
        return self.nombre
