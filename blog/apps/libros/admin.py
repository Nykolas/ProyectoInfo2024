from django.contrib import admin

from .models import Libro,Autor

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha_publicacion',)
    search_fields = ('isbn','titulo',)


admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor)