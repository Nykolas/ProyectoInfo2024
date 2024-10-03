
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('Registro/',views.RegistroUsuario.as_view(), name = 'registro_usuario'),

]
