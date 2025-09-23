from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_orden = models.IntegerField(default=0)
    descripcion = models.TextField(default='')

    def __str__(self):
        return self.nombre