from django import forms
from . models import Cabaña

class CabañaForm(forms.ModelForm):
    class Meta:
        model = Cabaña
        fields = "__all__"
        exclude = ['status']
        labels = {
            'imagen': 'Imagen',
            'nombre': 'Nombre',
            'capacidad': 'Capacidad',
            'descripcion': 'Descripcion',
            'comodidades': 'Comodidades',
            'tipocabaña': 'Tipocabaña',                      
        }
        widgets = {
            # 'imagen': forms.FileInput(attrs={'placeholder': 'Ingrese imagen'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'capacidad': forms.NumberInput(attrs={'placeholder': 'Ingrese capacidad'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingrese descripcion'}),
            'comodidades': forms.SelectMultiple(attrs={'placeholder': 'Ingrese comodidad'}),
            'tipocabaña': forms.SelectMultiple(attrs={'placeholder': 'Ingrese tipo de cabaña'})
            
            
                       
        }