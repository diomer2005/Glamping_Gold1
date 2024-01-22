from django import forms
from . models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = "__all__"
        exclude = ['status']
        labels = {
            'fecha': 'Fecha',
            'valor': 'Valor',
                                 
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'valor': forms.NumberInput(attrs={'placeholder': 'Ingresa el valor'}),
                      
        }