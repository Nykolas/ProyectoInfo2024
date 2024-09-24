from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Libro, Autor

def ListarLibros(request):

    # EQUIVALENTE EN SQL A UN: SELECT * FROM Libro
    #todos = Libro.objects.all()

    #Equivalente en SQL a UN: SELECT * FROM Libro WHERE titulo = 'Programacion 1'
    #algunos = Libro.objects.filter(titulo = 'Programacion 1')

    # TRAER TODOS LOS LIBROS DE UN AUTOR
    #BUSCO EL AUTOR
    #autor_buscado = Autor.objects.get(id = 1)
    #libros_x_autor = Libro.objects.filter(autor = autor_buscado)

    #CREAR UN OBJETO Y GUARDARLO EN LA BD.
    #a = Autor(nombre = 'Martin', apellido = 'Sena')
    #a.save()

    #MODIFCAR
    #a = Autor.objects.get(id = 1)
    #a.apellido = 'Perez'
    #a.save()

    #BORRAR
    #a = Autor.objects.get(id=3)
    #a.delete()

    ctx = {}
    todos = Libro.objects.all()
    ctx['libros'] = todos   

    #EL TEMPLATE listar VA A RECIBIR UNA VARIABLE QUE SE LLAME 
    #libros que va a contener la lista de libros (lo que esta en todos)

    #Es decir que el diccionario ctx se desempaqueta cada clave valor como una variable separada en el html

    #POR EJEMPLO
    #ctx['libros'] = todos_libros
    #ctx['autores'] = todos_autores
    #ctx['fecha'] = fecha_de_hoy
    #EN EL HTML LO QUE VOY A RECIBIR SON 3 VARIABLES SEPARADAS
    #una variable se llamara libros
    #la otra autores
    #y la otra fecha
    return render(request,'libros/listar.html',ctx)


class ListarLibros_clase(ListView):
    model = Libro
    template_name = 'libros/listar_clase.html'
    #POR DEFECTO, LOS OBJETOS SE PASAN AL TEMPLATE, 
    #BAJO UNA VARIABLE LLAMADA object_list

# DETALLE DE UN LIBRO

#VBF
def DetalleLibro(request,pk):
    libro = Libro.objects.get(pk = pk)
    ctx = {}
    ctx['libro'] = libro
    return render (request,'libros/detalle.html',ctx)

#VBC
class DetalleLibro_clase(DetailView):
    model = Libro
    template_name = 'libros/detalle_clase.html'
    #POR DEFECTO, LOS OBJETOS SE PASAN AL TEMPLATE, 
    #BAJO UNA VARIABLE LLAMADA object