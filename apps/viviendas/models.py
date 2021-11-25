from django.db import models

from apps.propietarios.models import Propietario


class Vivienda(models.Model):   
    direccion = models.CharField(max_length=100, verbose_name="Direccion")
    barrio = models.CharField(max_length=100, verbose_name="Barrio")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    def __str__(self):  
        return self.direccion
    class Meta: 
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"
