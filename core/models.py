from django.db import models

# Create your models here.
class Producto(models.Model):
    producto = models.CharField(max_length=25, blank=False, null=False)
    descripcion = models.CharField(max_length=50)
    precio = models.CharField(max_length=7)
    


# FORMULARIO CONTACTO
opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre