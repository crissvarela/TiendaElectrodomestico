from django.contrib import admin
from .models import Pelicula,Genero,Author

# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Genero)
admin.site.register(Author)