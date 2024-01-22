from django import forms
from . models import Cabaña
from comodidades.models import Comodidad
from tipocabañas.models import Tipocabaña


class CabañaForm(forms.ModelForm):
    comodidades = forms.ModelChoiceField(queryset=Comodidad.objects.filter(status = True).order_by('status'))
    tipocabaña = forms.ModelChoiceField(queryset=Tipocabaña.objects.filter(status = True).order_by('status'))
    class Meta:
        model = Cabaña
        fields = "__all__"
        exclude = ['status',]
        labels = {
            'imagen':'Imagen',
            'nombre': 'Nombre',
            'capacidad': 'Capacidad',
            'descripcion' : 'Descripcion',
            'comodidades' : 'Comodidades',
            'tipocabaña' : 'Tipocabaña'
                                 
        }
        widgets = {
            'imagen': forms.FileInput(attrs={'placeholder': 'Ingrese imagen de la cabaña'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'capacidad': forms.NumberInput(attrs={'placeholder': 'Ingresa la capacidad'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingresa la descripcion'}),  
            'comodidades': forms.CheckboxInput(attrs={'placeholder': 'Seleccione comodidades'}),          
            'tipocabaña': forms.SelectMultiple(attrs={'placeholder': 'Seleccione tipo de cabaña'}),
        }