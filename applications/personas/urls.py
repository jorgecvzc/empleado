from django.contrib import admin
from django.urls import path

from . import views
    
app_name = 'persona_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar_todos_empleados/', views.ListAllEmpleados.as_view(),name='empleados_all'),
    path('listar_by_area/<shortname>/', views.ListByArea.as_view(), name='empleados_area'),
    path('listar_by_trabajo/<shortname>/', views.ListByTrabajo.as_view()),
    path('buscar_empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar_habilidades_e/', views.ListHabilidades.as_view()),
    path('ver_empleado/<pk>/', views.EmpleadoDetailView.as_view(), name="empleado_detalle"),
    path('crear_empleado/', views.EmpleadoCreateView.as_view(), name="empleado_crear"),    
    path('success', views.SuccessView.as_view(), name='correcto'),
    path('unsuccess', views.UnsuccessView.as_view(), name='incorrecto'),
    path('update_empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('borrar_empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='borrar_empleado'),
]
