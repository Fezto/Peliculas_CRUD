#? Inicializador de la mayoría de las dependencias. Genera la instancia de Flask e inicializa
#? todas las dependencias que requieran de dicha instancia para funcionar.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

import os
from dotenv import load_dotenv
from .encoder import TimeEncoder

#* Generamos la instancia de Flask
app = Flask(__name__)

#* Traemos las credenciales de nuestro .env
load_dotenv()

#* Configuramos la llave secreta para el funcionamiento de Flask-WTF y Flask-SQLAlchemy
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.json = TimeEncoder(app)


MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_HOST = os.getenv("MYSQL_HOST") or "localhost"
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME") or "root"

if os.getenv("DOCKER") == "on":
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{MYSQL_ROOT_PASSWORD}@db/{MYSQL_DATABASE}'
else:
    #* Configuramos la conexión de la app hacia la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_ROOT_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}'

bootstrap = Bootstrap5(app)
database = SQLAlchemy(app)

#* Una vez lista la app, traer todas las rutas desde routes.py
from app import routes
