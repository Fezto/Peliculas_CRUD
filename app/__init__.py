from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

app.config['SECRET_KEY'] = "unstringdificildeadivinar"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Spongebob400!@localhost/chacharitas'

bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)

from app import routes
