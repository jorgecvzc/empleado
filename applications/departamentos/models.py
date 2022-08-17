from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Departamento (models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True)
    shortName = models.CharField('Nombre Corto', max_length=15, unique=True)
    anulate = models.BooleanField('Anulado', default=False)
    
    class Meta:
        verbose_name = 'Mi departamento' 
        verbose_name_plural = 'Mis departamentos'
        ordering = ['shortName', 'name']
        unique_together = ('name', 'shortName')
        
    def __str__ (self):
        return str(self.id) + ' - ' + 'Nombre: ' + self.name + ', ' + 'Nombre Corto:' + self.shortName
