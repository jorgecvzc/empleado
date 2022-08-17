from django import forms
from .models import Empleado, Habilidades

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = (
            'firstName',
            'lastName',
            'job',
            'departamento',
            'foto',
            'habilidades',
            )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }

