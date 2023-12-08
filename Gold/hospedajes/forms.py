from django import forms
from . models import Hospedaje

class HospedajeForm(forms.ModelForm):
    class Meta:
        model = Hospedaje
        fields = "__all__"
        exclude = ['status']
        labels = {
            'fecha': 'Fecha',
            'total': 'Total',
            'fechaInicio': 'Fecha de inicio',  
            'fechaFin': 'Fecha fin',
            'Cabaña': 'Cabaña',
            'Cliente': 'Cliente'                    
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'placeholder': 'Ingresa la fecha del dia que se creó el hospedaje'}),
            'total': forms.TextInput(attrs={'placeholder': 'Ingrese el total'}),
            'fechaInicio': forms.DateInput(attrs={'placeholder': 'Ingresa la fecha que deseas iniciar tú hospedaje'}), 
            'fechaFin': forms.DateInput(attrs={'placeholder': 'Ingresa la fecha que deseas terminar tú hospedaje'}),
            ''           
        }