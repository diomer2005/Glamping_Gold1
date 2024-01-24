from django import forms
from . models import Hospedaje
from clientes. models import Cliente
from cabañas. models import Cabaña

class HospedajeForm(forms.ModelForm):
    Cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(status = True).order_by('nombre'))
    Cabaña = forms.ModelChoiceField(queryset=Cabaña.objects.filter(status = True).order_by('nombre'))
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
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'total': forms.TextInput(attrs={'placeholder': 'Ingrese el total'}),
            'fechaInicio': forms.DateInput(attrs={'type': 'date'}), 
            'fechaFin': forms.DateInput(attrs={'type': 'date'}),
            'cabaña': forms.SelectMultiple(attrs={'placeholder': 'Seleccione una cabaña'}),         
            'cliente': forms.SelectMultiple(attrs={'placeholder': 'Seleccione un cliente'}),
        }