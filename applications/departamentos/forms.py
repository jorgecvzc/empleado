from django import forms

class NewDepartamentoForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=150)
    departamento = forms.CharField(max_length=80)
    shortname = departamento = forms.CharField(max_length=20)
    
                                 