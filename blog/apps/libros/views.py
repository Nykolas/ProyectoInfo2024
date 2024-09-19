from django.shortcuts import render

def ListarLibros(request):
    return render(request,'libros/listar.html')
