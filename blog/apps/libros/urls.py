
from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('listar/',views.ListarLibros, name = 'listar_libros'),

]
