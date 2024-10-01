
from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('listar/<str:nombre>/',views.ListarLibros, name = 'listar_libros'),
    path('listar_c', views.ListarLibros_clase.as_view(), name = 'listar_libros_clase'),

    path('detalle/<int:pk>',views.DetalleLibro, name = 'detalle_libro'),
    path('detalle_c/<int:pk>',views.DetalleLibro_clase.as_view(), name = 'detalle_libro_clase'),

    path('crear/', views.CrearLibro.as_view(), name = 'crear_libro'),
    path('modificar/<int:pk>', views.ModificarLibro.as_view(), name = 'modificar_libro'),

    path('eliminar/<int:pk>', views.EliminarLibro.as_view(), name = 'eliminar_libro'),

]
