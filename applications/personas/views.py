from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect
from .models import Empleado    
from django.views.generic.edit import CreateView
# Forms
from .forms import EmpleadoForm
# Create your views here.

class InicioView (TemplateView):
    ''' Vista que carga la página de inicio '''
    template_name = 'inicio.html'

# 1 - Listar todos los empleados de la empresa
class ListAllEmpleados (ListView):
    template_name = 'personas/list_all.html'
    paginate_by = 4 # 5 - Paginaciión de un listado
    ordering = 'lastName'
    context_object_name = 'empleados'
    
    def get_queryset (self):
        palabraClave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            fullName__icontains = palabraClave 
        )
        return lista

# 2 - Listar empleados de un área
class ListByArea (ListView):
    template_name = 'personas/list_all.html'
    context_object_name = 'empleados'
    
    def get_queryset (self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__shortName = area 
        )
        return lista


# 3 - Listar empleados por trabajo
class ListByTrabajo (ListView):
    template_name = 'personas/list_all.html'
    contect_object_name = 'listaArea'
    
    def get_queryset (self):
        trabajo = smelf.kwargs['shortname']
        
        lista = Empleado.objects.filter(
            job = trabajo
        )
        
        if not lista:
            lista = Empleado.JOB_CHOICES
            
        return lista

# 4 - Listar empleados por palabra clave
class ListEmpleadosByKword (ListView):
    """ Lista empleados por palabra clave """
    template_name = 'personas/persona_by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset (self):
        palabraClave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            firstName = palabraClave 
        )
        return lista
    
# 5 - Listar habiliades de un empleado
class ListHabilidades (ListView):
    template_name = 'personas/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        idEmpleado = self.request.GET.get('idEmpleado','')
        if idEmpleado:
            empleado = Empleado.objects.get(id=idEmpleado)
            return empleado.habilidades.all()
        else:
            return []


class EmpleadoDetailView (DetailView):
    model = Empleado
    template_name = 'personas/detail_empleado.html'
    context_object_name = 'empleados'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.object.fullName
        
        return context


class SuccessView (TemplateView):
    template_name = 'personas/success.html'

class UnsuccessView (TemplateView):
    template_name = 'personas/unsuccess.html'
    
class EmpleadoCreateView (CreateView):
    template_name = 'personas/add.html'
    model = Empleado
    form_class = EmpleadoForm

    success_url = reverse_lazy('persona_app:empleado_crear')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.fullName = empleado.firstName + ' '+ empleado.lastName
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView (UpdateView):
    template_name = 'personas/update.html'
    model = Empleado
    fields = ['firstName', 'lastName', 'job', 'departamento', 'habilidades']
    
    success_url = reverse_lazy('persona_app:empleados_all')
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print (request.POST['firstName'])
        return super().post (request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView (DeleteView):
    model = Empleado
    template_name = 'personas/delete.html'
    success_url = reverse_lazy('persona_app:empleados_all')
    unsuccess_url = '/unsuccess'
    
    def form_valid(self, form):
        success_url = self.get_success_url()
        object = self.get_object()
        lFirstName = object.firstName
        lista = Empleado.objects.filter(
            firstName = lFirstName 
        )
        if lista.count() > 1:
            return HttpResponseRedirect(self.unsuccess_url)
        else:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        
                
                