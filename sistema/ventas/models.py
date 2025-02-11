from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_cliente = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Clientes'

    def __str__(self):
        return f'{self.id_cliente} -- {self.nombre} -- {self.apellido}'