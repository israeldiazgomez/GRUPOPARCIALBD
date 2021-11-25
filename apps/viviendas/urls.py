from django.urls import path, include
from apps.viviendas.views import index,viviendaCreate,viviendaDelete,viviendaEdit

app_name = "viviendas";

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', viviendaCreate, name='viviendaCreate'),
    path('actualizar/<int:id_vivienda>/', viviendaEdit, name='viviendaEdit'),
    path('eliminar/<int:id_vivienda>/', viviendaDelete, name='viviendaDelete'),
]
