from django.db import models

# Create your models here.

class Producto(models.Model):
    # Definimos las opciones de categoría como una tupla de tuplas.
    # Cada tupla contiene dos elementos: el valor almacenado en la base de datos y la etiqueta visible para el usuario.
    CATEGORIA_CHOICES = (
    ('alimentos', 'Alimentos'),
    ('snacks', 'Snacks'),
    ('bebidas', 'bebidas'),
    ('ropa', 'Ropa'),
    ('zapatos', 'Zapatos'),
    ('maquillaje', 'Maquillaje'),
    ('deportes', 'Deportes'),
    ('electrodomesticos', 'Electrodomésticos'),
    ('limpieza', 'Limpieza'),
    ('higiene_personal', 'Higiene Personal'),
    ('cuidado_hogar', 'Cuidado del Hogar'),
    ('tecnolgia', 'Tecnología')
    )


    id_producto = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')  
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, verbose_name='Categoría')
    stock = models.IntegerField(verbose_name='Cantidad en stock')


    def __str__(self):
        return  "{} - {}".format(self.nombre, self.categoria)


'''
Alimentos > chocolates, galletas, pasteles.
Belleza > cremas antiedad, ácido hialurónico, crema de ojos, limpiadores faciales.
Deportes > Ropa deportiva, pesas, ligas, pelotas y balones.
Electrodomésticos > lavadoras, microondas, aspiradoras.
Higiene y salud > medicamentos, suplementos alimenticios, vitaminas, shampoo.
Maquillaje > labiales, base, rubores, delineadores.
Ropa > vestidos, pantalones, trajes de baño.
Tecnología > televisores, sonido, laptops y computadoras
'''