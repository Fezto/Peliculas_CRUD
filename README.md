# CRUD_Flask_PI
 Un CRUD basado en Flask fusionado épicamente con un poco de JavaScript

## Instalación

### 1. Instalación con Docker

El objetivo de esta instalación es el de terminar con un directorio similar al siguiente
```
C:.
├───mysql-data
│   └───  # Tu base de datos
├───.dockerignore
├───.env
├───docker-compose.yaml
├───DumpPeliculas.sql
└───wait-for-it.sh
```

Puedes obtener una plantilla ya generada y lista para su ejecución [aquí](https://github.com), en donde solo requerirás ejecutar el siguiente comando dentro de tu carpeta donde contengas todos los archivos.
```bash
docker-compose up
```

Si gustas, por supuesto puedes realizarlo manualmente

#### a. Instala la imagen del CRUD
Instala la imagen de la aplicación de Flask como lo harías con cualquier otra imagen
```bash
docker pull ayrtonsch/crud_flask_pi
```

#### b. Genera tu archivo .env
Luego, genera un archivo ``.env``. Puedes copiar el siguiente fragmento y pegarlo.

```
DOCKER=on                   # No cambiar
ORIGIN=mysql                # No cambiar
MYSQL_DATABASE=peliculas    # No cambiar

MYSQL_ROOT_PASSWORD=abc     # Cambiar
```

#### c. Descarga el archivo de volcado
Este será el que contiene todo el código SQL para la generación de los registros


#### d. Genera tu archivo docker-compose.yaml
Este será el encargado de ejecutar el contenedor de la app previamente instalada junto con una imagen de MySQL. Este lo puedes realizar de muchas maneras, aquí se te presenta una propuesta

```
services:
  web:
    image: ayrtonsch/crud_flask_pi
    command: ["./wait-for-it.sh", "db:3306", "--timeout=30", "--", "flask", "run", "--host=0.0.0.0"]
    ports:
      - 5000:5000
    depends_on:
      - db
    restart: on-failure
    env_file:
      - .env

  db:
    image: mysql:8.4.0
    command: --init-file /docker-entrypoint-initdb.d/DumpPeliculas.sql
    volumes:
      - ./mysql-data:/var/lib/mysql
      - ./DumpPeliculas.sql:/docker-entrypoint-initdb.d/DumpPeliculas.sql
    env_file:
      - .env
```



### 2. Instalación local
Primero ingresa en la carpeta donde quieras que se ubique el proyecto e ingresa el siguiente comando
```bash
git clone https://github.com/Fezto/CRUD_Flask_PI.git
```
Una vez instalado, abre el directorio en tu IDE de elección.

### 2. Instalación de las librerías
Una vez dentro, inserta el siguiente comando para descargar todas las librerías de Python necesarias del proyecto, las cuales se encuentran en ``requirements.txt``
```bash
pip install -r requirements.txt
```
Todas las librerías por la parte de JavaScript son importadas mediante CDNs, por lo que **una conexión a internet es obligatoria**

### 3. Ingresa al archivo ``.env``
Dentro de tu IDE agrega en la carpeta raíz tu archivo ``.env`` con las variables que se encuentran a continuación
```bash
# Escoge entre mysql y sqlserver
DB_ORIGIN=mi_smdb

# Inserta tus datos de acorde lo necesites.
# sqlserver solo requiere los primeros dos en caso de usar autenticación por windows.

DB_HOST=localhost         # Por lo general será siempre localhost
DB_NAME=mi_base_datos     # El nombre de tu base de datos
DB_USER=mi_usuario        # El nombre de su usuario
DB_PASS=mi_contraseña     # La contraseña de tu usuario

# Configura un string que será tu llave CSRF secreta
SECRET_KEY=un_string_dificil_pero_necesario

# El nombre de la app. Este no cambia.
FLASK_APP=app.py

```

### 4. Ejecuta el programa
Para correr el programa solo basta con utilizar el siguiente comando
```bash
flask run
```
E ingresa en la liga que se te presenta a continuación.

Para activar el hot reload y para tener una mejor experiencia si quieres experimentar con la ap, no se te olvide activar la opción ``debug``
```bash
flask run --debug
```