from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('productos/', views.lista_productos, name='listado'),
    path('productos/nuevo/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:id>/editar', views.editar_producto, name='editar_producto'),
    path('productos/<int:id>/eliminar', views.eliminar_producto, name='eliminar_producto'),
    path('productos/info', views.info, name='info')
    
]
