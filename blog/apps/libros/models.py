from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length = 80)
    apellido = models.CharField(max_length = 80)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'


class Categoria(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length = 200)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE, null = True)
    imagen = models.ImageField(upload_to='libros', null = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.titulo

