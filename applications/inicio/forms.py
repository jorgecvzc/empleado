from django import forms
from .models import Prueba

class PruebaForm (forms.ModelForm):
    
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
        
        widgets = {
            'titulo': forms.TextInput (
                attrs = {'placeholder': 'Introduzca texto'
                         }
            )
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('La cantidad ha de ser mayor de 9')
    
        return cantidad
    
