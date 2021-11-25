from django import forms
from django.forms import fields
from django import forms
from apps.propietarios.models import Propietario

class PropietarioForm(forms.ModelForm):   
    class Meta:   
        model = Propietario
        
        fields = [
             'nombre',
             'apellido',
             'fecha',
             'codigo'
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha': 'Fecha',
            'codigo': 'Codigo'
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
        }