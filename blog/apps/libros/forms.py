
from django import forms
from .models import Libro

class FormularioCrearLibro(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('titulo','fecha_publicacion','isbn','autor','imagen')


class FormularioModificarLibro(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('isbn','autor','imagen','categoria')
