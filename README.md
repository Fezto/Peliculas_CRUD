# CRUD_Flask_PI
 Un CRUD basado en Flask fusionado épicamente con un poco de JavaScript

## Instalación

### I. Instalación con Docker
Esta versión utiliza dos imagenes precargadas en Docker Hub con todo lo necesario para poder utilizar el CRUD. Sigue los pasos a continuación 

#### a. Descarga las imagenes desde Docker Hub

En un ``cmd`` o ``bash``, ejecuta los siguientes comandos
```bash
docker pull ayrtonsch/peliculas_crud
docker pull ayrtonsch/peliculas_bd
```

#### b. Genera un directorio nuevo
Haz una nueva carpeta en el lugar que desees.

#### c. Genera un archivo ``docker-compose.yaml``
Crea un archivo``docker-compose.yaml``, el cual nos servirá para que ejecutemos ambos contenedores. **¡Puedes copiar y pegar esto sin problemas!**

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

#### d. Descarga el archivo ``wait-for-it.sh``
Este pequeño script permitirá que el contenedor con el CRUD se ejecute cuando la base de datos está lista. Puedes instalar el script de este mismo repositorio o del repositorio original [aquí](https://github.com/vishnubob/wait-for-it)

#### e. ¡Ejecuta el programa!
Con tu archivo ``wait-for-it.sh`` y ``docker-compose.yaml`` dentro de un directorio, llego la hora de ejecutar el siguiente comando:
```bash
docker-compose up
```
Si es tu primera vez ejecutando, Docker tendrá que jalar las imagenes en línea desde Docker Hub y tardará aproximadamente unos 30 segundos en ejecutarse.

#### d. ¿Error?
Si te  aparece un error lo más probable es que sea porque el puerto 5000, el cual utiliza Flask por defecto, está ocupado por algun otro proceso de tu Sistema Operativo

### II. Instalación local
#### a. Clonación del proyecto
Primero ingresa en la carpeta donde quieras que se ubique el proyecto e ingresa el siguiente comando
```bash
git clone https://github.com/Fezto/CRUD_Flask_PI.git --config core.autocrlf=input
```
Una vez instalado, abre el directorio en tu IDE de elección.

#### 2. Instalación de las librerías
Una vez dentro, inserta el siguiente comando para descargar todas las librerías de Python necesarias del proyecto, las cuales se encuentran en ``requirements.txt``
```bash
pip install -r requirements.txt
```
Todas las librerías por la parte de JavaScript son importadas mediante CDNs, por lo que **una conexión a internet es obligatoria**

#### 3. Generamos un archivo ``.env``
Dentro de tu IDE agrega en la carpeta raíz tu archivo ``.env`` con las variables que se encuentran a continuación
```
# Inserta tus datos de acorde lo necesites..
DB_NAME=your_database        # OBLIGATORIO: El nombre de tu base de datos
DB_PASS=your_password        # OBLIGATORIO: La contraseña de tu usuario
DB_USER=your_username        # [OPCIONAL]: Por default configurado como "root"
DB_HOST=your_host_ip         # [OPCIONAL]: Por default configurado como "localhost"
                             #             Si quieres dockerizar, debe ser "db"

# Configura un string que será tu llave CSRF secreta
SECRET_KEY=un_string_dificil_pero_necesario  # OBLIGATORIO

# El nombre de la app. Este no cambia.
FLASK_APP=app.py    # OBLIGATORIO

```

#### 4. Ejecuta el programa
Para correr el programa solo basta con utilizar el siguiente comando
```bash
flask run
```
E ingresa en la liga que se te presenta a continuación.

Para activar el hot reload y para tener una mejor experiencia si quieres experimentar con la ap, no se te olvide activar la opción ``debug``
```bash
flask run --debug
```