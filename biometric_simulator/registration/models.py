from django.db import models
from django.utils.timezone import datetime
from employee.models import Employee, Fingerprint

# Create your models here.

class Register (models.Model):
    date = models.DateField('Fecha', auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    #employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Empleado')
    fingerprint = models.ForeignKey(Fingerprint, on_delete=models.CASCADE, verbose_name='Huella dactilar', null=True)

    def __str__(self):
        cadena = 'Fecha: {0}, Hora de Entrada: {1}, Empleado: {2}'
        return cadena.format(self.date, self.time, self.fingerprint.employee.__str__())

    class Meta:
        db_table = 'register'
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'