from django.contrib import admin
from .models import Producto, Contacto, ContactoReal

# Register your models here.

admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(ContactoReal)