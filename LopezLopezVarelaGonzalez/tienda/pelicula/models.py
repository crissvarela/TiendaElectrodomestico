from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=400)
    autor = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey('Genero', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.titulo

    def get_absolute_url (self):
        return reverse('pelicula_detail',args=[str(self.id)])

class Author(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_producida = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ['nombre', 'apellido']

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'