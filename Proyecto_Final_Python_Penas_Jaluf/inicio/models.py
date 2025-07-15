from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=30)
    anio = models.IntegerField()

    def __str__(self):
        return f'Marca: {self.marca}, Descripción: {self.descripcion}, Año: {self.anio}'

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=30)
    anio = models.IntegerField()

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Descripción: {self.descripcion}, Año: {self.anio}'

class Moto(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=30)
    anio = models.IntegerField()

    def __str__(self):
        return f'Marca: {self.marca}, Descripción: {self.descripcion}, Año: {self.anio}'
    