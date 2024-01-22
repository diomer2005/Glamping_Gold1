from django import forms
from . models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
        exclude = ['status']
        labels = {
            'nombre': 'Nombre',
            'valor': 'Valor',                     
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'valor': forms.TextInput(attrs={'placeholder': 'Ingresa el valor'}),
              
        }