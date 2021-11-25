from django.urls import path, include
from apps.propietarios.views import propietarioCreate,propietarioDelete,propietarioEdit,index

app_name = "propietarios";

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', propietarioCreate, name='propietarioCreate'),
    path('actualizar/<int:id_propietario>/', propietarioEdit, name='propietarioEdit'),
    path('eliminar/<int:id_propietario>/', propietarioDelete, name='propietarioDelete'),
]
