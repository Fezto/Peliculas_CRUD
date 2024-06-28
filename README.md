# CRUD_Flask_PI
 Un CRUD basado en Flask fusionado épicamente con un poco de JavaScript

## Instalación

Por el momento, la ejecución del programa con Docker solo es soportada con MySQL mientras que la instalación local soporta MySQL y SQLServer

### 1. Instalación con Docker

Puedes realizar algunas de las dos instalaciones con docker:
 * La automática, la cual es la más rápida y más sencilla
 * La manual, la cual es más personalizable pero más tardada

#### a. Automática
Esta versión utiliza dos imagenes precargadas en Docker Hub con todo lo necesario para poder utilizar el CRUD con una base de datos de Películas. Lo unico necesario es que hagas un directorio y que ahí generes un archivo ``docker-compose.yaml`` que ejecute ambos contenedores. **¡Puedes copiar y pegar esto sin problemas!**

```
services:
  web:
    image: ayrtonsch/peliculas_crud
    command: ["./wait-for-it.sh", "db:3306", "--timeout=30", "--", "flask", "run", "--host=0.0.0.0"]
    ports:
      - 5000:5000
    depends_on:
      - db
    restart: on-failure

  db:
    image: ayrtonsch/peliculas_db
```

Se recomienda también descargar el script de bash ``wait-for-it.sh``, ya que este permitirá que el contenedor con el CRUD se ejecute cuando la base de datos está lista. Puedes instalar el script de este mismo repositorio o del repositorio original [aquí](https://github.com/vishnubob/wait-for-it)

Con tu archivo ``wait-for-it.sh`` y ``docker-compose.yaml`` dentro de un directorio, llego la hora de ejecutar el siguiente comando:
```bash
docker-compose up
```
Si es tu primera vez ejecutando, Docker tendrá que jalar las imagenes en línea desde Docker Hub y tardará aproximadamente unos 30 segundos en ejecutarse.


#### b. Manual
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
### -- Continuará ----


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
# Escoge entre MySQQ o SQLServer
ORIGIN=mysql

# Inserta tus datos de acorde lo necesites..
DB_NAME=your_database        # OBLIGATORIO: El nombre de tu base de datos
DB_PASS=your_password        # OBLIGATORIO: La contraseña de tu usuario
DB_HOST=your_host_ip         # [OPCIONAL]: Por default configurado como "localhost"
DB_USER=your_username        # [OPCIONAL]: Por default configurado como "root"

# Configura un string que será tu llave CSRF secreta
SECRET_KEY=un_string_dificil_pero_necesario  # OBLIGATORIO

# El nombre de la app. Este no cambia.
FLASK_APP=app.py    # OBLIGATORIO

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