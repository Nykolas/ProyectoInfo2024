
from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('listar/',views.ListarLibros, name = 'listar_libros'),

    path('listar_c', views.ListarLibros_clase.as_view(), name = 'listar_libros_clase'),

]
