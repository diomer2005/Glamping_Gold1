from django import forms
from . models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model =Cliente
        fields = "__all__"
        exclude = ['status']
        labels = {
           'nombre':'Nombre',
           'documento':'Documento',
           'nacionalidad':'Nacionalidad',
           
                              
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresar nombre'}),
            'documento': forms.NumberInput(attrs={'placeholder': 'Ingrser su documento'}),
            'nacionalidad': forms.TextInput(attrs={'placeholder': 'Ingrese la nacionalidad'})
            


        }