# Fase3_LopezLopezVarelaGonzalez

credenciales de Administrador
usuario: admin
contraseña: admin

credenciales de Usuario
usuario: pelisview
contraseña: admin12345

rutas urls:

principales

http://127.0.0.1:8000/pelicula/
http://127.0.0.1:8000/pelicula/ranking/
http://127.0.0.1:8000/pelicula/contacto/ 

para detalle

http://127.0.0.1:8000/pelicula/pelicula/<int:pk>/
http://127.0.0.1:8000/pelicula/author/<int:pk>/

para lista

http://127.0.0.1:8000/pelicula/pelicula/
http://127.0.0.1:8000/pelicula/author/

para Crear/Borrar/Modificar

http://127.0.0.1:8000/pelicula/pelicula/create/
http://127.0.0.1:8000/pelicula/author/create/
http://127.0.0.1:8000/pelicula/pelicula/update/<int:pk>/
http://127.0.0.1:8000/pelicula/author/update/<int:pk>/
http://127.0.0.1:8000/pelicula/pelicula/delete/<int:pk>/
http://127.0.0.1:8000/pelicula/author/delete/<int:pk>/

para ingresar al Login

http://127.0.0.1:8000/accounts/login/

instalar en cmd
pip install djangorestframework
