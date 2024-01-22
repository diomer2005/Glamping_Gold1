from django import forms
from . models import Comodidad

class   ComodidadForm(forms.ModelForm):
    class Meta:
        model = Comodidad
        fields = "__all__"
        exclude = ['status']
        labels = {
            'nombre': 'Nombre',                   
        } 
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            }