
## Instalación
***
```
Título del Proyecto TestBike

Breve descripción de mi intento:
Creación de una vista en Django para mostrar la información de las estaciones 
de bicicletas públicas de Santiago (Ver enlace Tarea1).

Utilización de Bootstrap y sus clases para diseñar y presentar la información 
de las estaciones en una tabla  ordenable.

Implementación de un botón para actualizar los datos de las estaciones desde 
la API de manera que se reflejen los cambios en la base de datos.

Para la tarea 2, se creó una vista en Django que utiliza una función para 
obtener los datos de un archivo JSON y guardarlos en una base de datos
PostgreSQL.
Se utilizó el método get_or_create para evitar la creación de duplicados en la 
base de datos y se asignaron los datos de cada proyecto a un objeto de tipo 
Proyectos que fue guardado en la base de datos.

Luego, se creó una tabla en una vista de Django que muestra los datos de la 
base de datos utilizando el modelo Proyectos. Se importaron estilos de 
Bootstrap 5 para dar un estilo atractivo a la tabla.

Por último, se creó un botón en la vista que permite actualizar los datos
de la base de datos, obteniendo los nuevos datos del archivo JSON y 
sobrescribiendo los existentes.

En general, he ha utilizado Bootstrap y otras herramientas para mejorar el
diseño y la presentación de la información de todo el proyecto.

para control de versionado utilice git y fui realizando los commits a medida
que avanzaba en las tareas.

Instalación
    - Clonar el repositorio del proyecto o descargarlo en formato zip 
        https://github.com/DouglasGuacaran/testbike.git.
    - Instalar las dependencias del proyecto usando el archivo requirements.txt,
        comando: "python install -r requirements.txt"
    - Crear un entorno virtual y activarlo, el comando es comando: 
        "source env/bin/activate"
    - Configurar las variables de entorno necesarias (p. ej. credenciales de 
        base de datos).
    - Sera necesario crear en la carpeta testbike un archivo .env que contenga
        los valores de:
        SECRET_KEY=django-insecure-=s0ptp13ebrdoas4qzg8fn&kk+o=!*--_x*ev91_-*c$8$q9!a
        PASSWORD=(acá la clave de tu BD posgres)
        DEBUG= True
    - Realizar las migraciones de la base de datos "python manage.py migrate"
        "python manage.py.makemigrations"
    - Crear un superusuario para acceder al panel de administración 
        "python manage.py.createsuperuser"
    - Iniciar el servidor de desarrollo "python manage.py.runserver"
    - Acceder al proyecto en un navegador web.
