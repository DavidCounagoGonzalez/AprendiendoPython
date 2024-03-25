# Django

Tener python y pip instalados en el equipo (pip es un componente de python)
Crear una carpeta para el proyecto e ir a ella desde el cmd. Una vez hecho esto lanzamos el comando:
py -m pip install modulo_a_instalar (en este caso virtualenv)

Siguiendo sobre nuestro proyecto utilizamos el siguiente comando para instalar los archivos del módulo en nuestro proyecto:
py -m virtualenv venv
		El cuál creará la carpeta venv con su contenido.

Ahora lanzamos el script activate para activar el entorno:
.\venv\Scripts\activate
Para comprobarlo podremos lanzar python –version , que nos devolverá la versión de python que es exclusiva de este proyecto.

Abrimos el proyecto en VisualStudio pulsamos F1 y escribimos select interpreter y escogemos la versión de python con ruta sobre nuestro proyecto ( que debe salir como recommended). Esto hará que al abrir una consola de visual se abra en el entorno.

### Instalar Django:

Para instalar django utilizamos:
pip install django
Podemos comprobar comprobar que está instalado viendo su versión con :
py -m django –version

### Crear proyecto Django:
Para crear un proyecto de Django utilizaremos el siguiente comando para crear los archivos en nuestro proyecto:
django-admin startproject mysite .
Ahora para lanzar el servidor con nuestro proyecto usaremos el archivo mange.py que se creó en el punto anterior de la siguiente manera:
py manage.py runserver
		Esta ejecución debería devolver contra el final esta línea 
Starting development server at http://127.0.0.1:8000/ 
La cuál indica la url de tu proyecto django.

### Cambiar puerto Django:
Si ya existe una app en el puerto 8000 que es el por defecto, podemos cambiarlo añadiendo el puerto deseado tras runserver:
py manage.py runserver 8001 (o el que tu quieras)


### Base de Datos

Para cargar la BD por defecto que tare Django sobre nuestro archivo sqlite3 debemos lanzar en la terminal el comando
py manage.py migrate.

### Crear una clase nueva en nuestra BD
Para ello iremos al archivo models.py en myapp y crearemos una clase(ver archivo en el repo para referencia), para que la 
app reconozca el modelo creado iremos al archivo settings.py de mysite y buscaremos el apartado INSTALLED_APPS y añadiremos el nombre de la carpeta de nuestra app (en este caso myapp). Tras ello podremos lanzar las migraciones con:
- py manage.py makemigrations (opcional indicar la carpeta para que solo haga las existentes en el)
- py manage.py migrate (también se puede indicar la carpeta)

### Python en html

Para hacer uso de python en mitas de un archivo html nos valemos de {% %} y en caso de ser una variable pasada desde el render {{}}

Los comentarios sobre los html se encuentran en ![projects.html](https://github.com/DavidCounagoGonzalez/AprendiendoPython/blob/main/djangoProject/myapp/templates/projects/projects.html), excepto el ejemplo de utilizar un condcional que está en ![tasks.html](https://github.com/DavidCounagoGonzalez/AprendiendoPython/blob/main/djangoProject/myapp/templates/tasks/tasks.html)
