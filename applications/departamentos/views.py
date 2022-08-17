from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView

from .forms import NewDepartamentoForm 

from applications.personas.models import Empleado
from .models import Departamento

# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamentos/lista.html"
    context_object_name = 'departamentos'


class NewDepartamentoView  (FormView):
    template_name = 'departamentos/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        depart = Departamento(
            name = form.cleaned_data['departamento'],
            shortName = form.cleaned_data['shortname'],
        )
        depart.save()
        
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            firstName = nombre,
            lastName = apellido,
            job = 1,
            departamento = depart
        )
        return super(NewDepartamentoView, self).form_valid(form)
    
    