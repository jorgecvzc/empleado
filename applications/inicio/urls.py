from django.contrib import admin
from django.urls import path

from . import views
    
urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista_prueba/', views.ListaPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueb_add'),
    path('resumen_foundation/', views.ResumenFoundationView.as_view(), name='resumen_f')
]
