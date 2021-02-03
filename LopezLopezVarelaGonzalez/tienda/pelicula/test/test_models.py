from django.test import TestCase
from django.test.utils import get_runner
from  pelicula.models import Pelicula, Genero, Author



class PeliculaModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        peli=Pelicula.objects.create(titulo='Piratas del Caribe', 
        descripcion='la peliculaaaaaaaaaaaaaaaaaaa')


    def test_titulo_label(self):
        peli=Pelicula.objects.get(id=1)
        field_label = peli._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label,'titulo')

    def test_descripcion_label(self):
        peli=Pelicula.objects.get(id=1)
        field_label = peli._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label,'descripcion')




class GeneroModelTest(TestCase):

     @classmethod

     def setUpTestData(cls):
        g=Genero.objects.create(nombre='Accion')

     def test_nombre_label(self):
        g=Genero.objects.get(id=1)
        field_label = g._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

class AutorModelTest(TestCase):

     @classmethod

     def setUpTestData(cls):
        aut=Author.objects.create(nombre='Juan Ajedrez', apellido='lulula')


     def test_nombre_label(self):
        aut=Author.objects.get(id=1)
        field_label = aut._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

     def test_apellido_label(self):
        aut=Author.objects.get(id=1)
        field_label = aut._meta.get_field('apellido').verbose_name
        self.assertEquals(field_label,'apellido')
