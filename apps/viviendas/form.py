from django import forms
from django.forms import fields
from django import forms
from apps.viviendas.models import Vivienda

class ViviendaForm(forms.ModelForm):   
    class Meta:   
        model = Vivienda
        
        fields = [
             'direccion',
             'barrio',
             'propietario'
        ]
        labels = {
            'direccion': 'Direccion',
            'barrio': 'Barrio',
            'propietario': 'Seleccione propietario'
        }
        
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'barrio': forms.TextInput(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
        }