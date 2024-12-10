from django.urls import path

from app_coder import views

urlpatterns = [
    
     path("", views.inicio, name="inicio"),
    
    # URLs para Clientes
    path('clientes/', views.lista_clientes, name='clientes'),
    path('cliente-formulario/', views.cliente_formulario, name="cliente-formulario"),
    path('clientes/editar_cliente/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),

    # URLs para Comercios
    path('comercios/', views.lista_comercios, name='comercios'),
    path('comercio-formulario/', views.comercio_formulario, name="comercio-formulario"),
    path('comercios/editar_comercio/<int:pk>/', views.editar_comercio, name='editar_comercio'),
    path('comercios/eliminar/<int:pk>/', views.eliminar_comercio, name='eliminar_comercio'),

    # URLs para Productos
    path('productos/', views.lista_productos, name='productos'),
    path('producto-formulario/', views.producto_formulario, name="producto-formulario"),
    path('productos/editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/detalle-producto/<int:pk>/', views.detalle_producto_view, name='ver_info_producto'),
]