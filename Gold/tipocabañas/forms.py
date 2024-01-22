from django import forms
from . models import Tipocabaña

class TipocabañaForm(forms.ModelForm):
    class Meta:
        model = Tipocabaña
        fields = "__all__"
        exclude = ['status']
        labels = {
            'nombre': 'Nombre',                     
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
                        
        }