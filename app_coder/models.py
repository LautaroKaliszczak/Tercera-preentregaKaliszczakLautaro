from django.db import models


from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Comercio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    tipo_comercio = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto,null=True, blank=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    mail = models.EmailField()
    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
