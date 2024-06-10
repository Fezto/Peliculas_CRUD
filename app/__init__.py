#? Inicializador de la mayoría de las dependencias. Genera la instancia de Flask e inicializa
#? todas las dependencias que requieran de dicha instancia para funcionar.

#* Flask: Nos permite realizar las solicitudes HTTP y manejar el backend con Python
#* Bootstrap-Flask: Permite incorporar Bootstrap de manera sencilla en una app de Flask
#* Flask-SQLAlchemy: Es un wrapper de SQLAlchemy que facilita y automatiza la conexión de DB con Flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

#* Generamos la instancia de Flask
app = Flask(__name__)

#* Configuramos la llave secreta para el funcionamiento de Flask-WTF y Flask-SQLAlchemy
app.config['SECRET_KEY'] = "unstringdificildeadivinar"

#* Configuramos la conexión de la app hacia la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Spongebob400!@localhost/chacharitas'

bootstrap = Bootstrap5(app)
database = SQLAlchemy(app)


#* Una vez lista la app, traer todas las rutas desde routes.py
from app import routes