from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length = 200)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo

