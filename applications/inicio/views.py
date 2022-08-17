from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.list import BaseListView

from .models import Prueba
from .forms import PruebaForm

# Create your views here.
class PruebaView (TemplateView):
    template_name = 'inicio/prueba.html'
    
class PruebaListView (ListView):
    template_name = 'inicio/lista.html'
    context_object_name = 'listaalfans'
    queryset =  ['a','10', 'c ', 'd']
    
class ListaPrueba (ListView):
    template_name = 'inicio/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'
    
class PruebaCreateView (CreateView):
    template_name = 'inicio/add.html'
    model = Prueba
    #fields = ['titulo', 'subtitulo', 'cantidad'] -> Se comenta para usar PruebaForm
    form_class = PruebaForm
    success_url = '/success'
    
    
class ResumenFoundationView (TemplateView):
    template_name = 'inicio/resumen_foundation.html'