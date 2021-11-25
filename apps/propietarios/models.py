from django.db import models


class Propietario(models.Model):   
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    fecha = models.DateField(verbose_name="Fecha")
    codigo = models.CharField(max_length=100, verbose_name="Codigo")
    
    # Verdadero = models.BooleanField()
    
    def __str__(self):  
        return self.nombre
    class Meta: 
        verbose_name = "Propietario"
        verbose_name_plural = "Propietarios"