from django.contrib import admin

# Register your models here.
from .models import Empleado, Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'firstName',
        'lastName',
        'departamento',
        'job',
        'fullName',
    )
    
    def fullName(self, obj):
        return obj.firstName + ' ' + obj.lastName
    
    search_fields = ('firstName', 'lastName')
    list_filter = ('job', 'lastName', 'habilidades', )
    
    filter_horizontal = ('habilidades',)
    
admin.site.register(Empleado, EmpleadoAdmin)    