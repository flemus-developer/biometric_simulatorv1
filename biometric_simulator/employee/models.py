from django.db import models

# Create your models here.

class Employee (models.Model):
    name = models.CharField('Nombre', max_length=10, help_text='Juan, María, Pedro')
    surname = models.CharField('Apellido', max_length=10, help_text='Morales, España, Gómez')
    email = models.EmailField('Correo Electrónico')
    state = models.BooleanField('Estado', default=True)

    def __str__(self):
        cadena = '{0} {1}'
        return cadena.format(self.name, self.surname)

    class Meta:
        db_table = 'employee'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class Fingerprint (models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Empleado')
    state = models.BooleanField(default=True, editable=False)

    def __str__(self):
        cadena = 'ID Huella: {0}, Empleado: {1}'
        return cadena.format(self.pk, self.employee.__str__())

    class Meta:
        db_table = 'fingerprint'
        verbose_name = 'Huella dactilar'
        verbose_name_plural = 'Huellas dactilares'
        unique_together = ['employee']