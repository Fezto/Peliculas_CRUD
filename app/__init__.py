#? Inicializador de la mayoría de las dependencias. Genera la instancia de Flask e inicializa
#? todas las dependencias que requieran de dicha instancia para funcionar.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

import os
from dotenv import load_dotenv

#* Generamos la instancia de Flask
app = Flask(__name__)

#* Traemos las credenciales de nuestro .env
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_ORIGIN = os.getenv("DB_ORIGIN")
DOCKER = os.getenv("DOCKER")

#* Configuramos la llave secreta para el funcionamiento de Flask-WTF y Flask-SQLAlchemy
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

#* Configuramos la conexión de la app hacia la base de datos
if DOCKER == "on":
    if DB_ORIGIN == "mysql":
        DB_HOST = "db"
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
else:
    if DB_ORIGIN == "mysql":
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
    elif DB_ORIGIN == "sqlserver":
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://@{DB_HOST}/{DB_NAME}?trusted_connection=yes&driver=ODBC+Driver+18+for+SQL+Server&Encrypt=no'

print(app.config)

bootstrap = Bootstrap5(app)
database = SQLAlchemy(app)

#* Una vez lista la app, traer todas las rutas desde routes.py
from app import routes


