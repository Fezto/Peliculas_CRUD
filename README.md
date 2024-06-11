# CRUD_Flask_PI
 Un CRUD basado en Flask fusionado épicamente con un poco de JavaScript

## Instalación

### 1. Clonación del Programa
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
Dentro de tu IDE modifica el archivo ``.env`` previamente mencionado con las credenciales de tu base de datos
```bash
DB_HOST=localhost     # Por lo general eso no cambia  
DB_NAME=chacharitas   # El nombre de la base de datos
DB_USER=root          # El nombre de usuario
DB_PASS=mi_pwd        # La contraseña de tu usuario
```

### 4. Ejecuta el programa
Para correr el programa solo basta con utilizar el siguiente comando
```bash
flask run
```
E ingresa en la liga que se te presenta a continuación.

Para activar el hot reload y para tener una mejor experiencia, no se te olvide activar la opción ``debug``
```bash
flask run --debug
```