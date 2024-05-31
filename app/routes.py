from flask import render_template, url_for, flash, send_from_directory, request, redirect

from app import app
from app.database import Database
from app.forms.modal_form import generate_dynamic_form

db = Database()

@app.route("/", methods=["GET"])
def start():
    return redirect(url_for("index", table=db.addresses))

@app.route("/index/<table>", methods=["GET", "POST"])
def index(table):
    if request.method == "GET":

        #* Para llenar las opciones en el <navbar> lateral
        tables = db.select_tables()

        #* Para el llenado del <table> y el <modal>
        table_columns = db.select_columns(table=db[table])
        table_body = db.select_all(table=db[table])
        table_columns_data = db.select_columns_data(db[table])

        #* Genera un formulario (clase) de FlaskWTF dinámicamente con las
        #* propiedades adecuadas por cada columna de la tabla. Este se
        #* insertará dentro del <modal>

        ModalForm = generate_dynamic_form(table_columns_data=table_columns_data, table_columns=table_columns, db=db)

        #* Instancia de la clase generada
        modal_form = ModalForm()

        return render_template('index.html', table_body=table_body, table_headers=table_columns, tables=tables, modal_form=modal_form)


