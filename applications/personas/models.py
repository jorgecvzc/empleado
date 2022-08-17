from django.db import models
from applications.departamentos.models import Departamento
# Create your models here.
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        
    def __str__ (self):
        return str(self.id) + ', ' + self.habilidad + '#'
    

class Empleado(models.Model):
    """ Modelo  para tabla empleado """
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('4', 'Otro')
        )
    firstName = models.CharField('Nombre', max_length=60)
    lastName = models.CharField('Apellidos', max_length=200)
    fullName = models.CharField(
        'Nombres Completos, ',
        blank = True,
        max_length=260
    )
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='empleados', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hojaVida = RichTextField()

        
    class Meta:
        verbose_name = 'El empleado'
        verbose_name_plural = 'Los empleados'
        ordering = ['lastName', 'firstName']
        unique_together = ('firstName', 'lastName')

    def __str__ (self):
        return str(self.id) + ' - ' + 'Nombre: ' + self.firstName+ ', ' + 'Apellidos:' + self.lastName
