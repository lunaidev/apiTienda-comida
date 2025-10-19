from django.db import models
import pyotp  # <-- Agrega esta línea

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_orden = models.IntegerField(default=0)
    descripcion = models.TextField(default="Sin descripción", blank=True)
    secret = models.CharField(max_length=32, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.secret:
            self.secret = pyotp.random_base32()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre