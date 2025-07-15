from django.db import models

class Trineo(models.Model):
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    anio = models.DateField()
    
    def __str__(self):
        return f'{self.marca} - {self.color}'
    