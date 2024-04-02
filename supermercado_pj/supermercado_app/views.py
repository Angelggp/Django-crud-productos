from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Producto
from .form import ProductoForm

# Create your views here.

def index(request):
    template = 'index.html'
    return render(request, template)

def lista_productos(request):
    template = 'producto_list.html'
    productos = Producto.objects.all()
    return render(request, template, {'productos': productos})

def agregar_producto(request):
    template = 'producto_form.html'
    producto_form = ProductoForm()
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            messages.success(request, 'Producto agregado!')
            return redirect('agregar_producto')
        else:
            messages.error(request, 'Ha ocurrido un error!')
            return redirect('agregar_producto')
    return render(request, template, {'form': producto_form})

def editar_producto(request, id):
    # Obtener el producto existente que se va a editar
    producto = get_object_or_404(Producto, pk=id)
    template = 'producto_form.html'
    
    # Verificar si la solicitud es de tipo POST
    if request.method == 'POST':
        # Crear una instancia del formulario y pasar los datos de la solicitud
        producto_form = ProductoForm(request.POST, instance=producto)
        if producto_form.is_valid():
            # Guardar los cambios en el producto
            producto_form.save()
            # Mostrar un mensaje de éxito
            messages.success(request, 'Producto actualizado exitosamente.')
            # Redirigir a algún lugar apropiado, como la lista de productos
            return redirect('listado')
        else:
            # Si el formulario no es válido, mostrar un mensaje de error
            messages.error(request, 'Ha ocurrido un error. Por favor, verifica los datos ingresados.')
            # Puedes renderizar el formulario nuevamente para que el usuario pueda corregirlo
            return render(request, template, {'form': producto_form})
    else:
        # Si la solicitud no es de tipo POST, simplemente mostrar el formulario con los datos actuales del producto
        producto_form = ProductoForm(instance=producto)
        return render(request, template, {'form': producto_form})
    
    
def eliminar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    return redirect('listado')

def info(request):
    template = 'info.html'
    return render(request, template)