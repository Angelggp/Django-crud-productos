from django import forms 
from .models import Producto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))
        self.helper.form_class = 'form-control'  # Agregar la clase 'form-control' de Bootstrap al formulario
        self.helper.layout = Layout(
            'nombre',
            'descripcion',  # 'descripcion' es el nombre del campo en tu modelo
            'precio',
            'categoria',
            'stock',
        )

        # Definir clases adicionales para el campo 'descripcion' para controlar el tamaño del textarea
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control my-textarea', 'rows': 3})  

    class Meta:
        model = Producto
        fields = ('nombre','descripcion', 'precio', 'categoria', 'stock' )
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'categoria': 'Categoría',
            'stock': 'Cantidad en stock'
        }