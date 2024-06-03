from flask import render_template, url_for, flash, send_from_directory, request, redirect, jsonify

from app import app
from app.database import Database
from app.forms.modal_form import generate_dynamic_form

#* Instancia para el contacto con nuestra base de datos
db = Database()

#* Para llenar las opciones en el <navbar> lateral
tables = db.select_tables()


#* Rutas principales. Estas son las que responden ante
#* las solicitudes HTTP del cliente.
@app.route("/", methods=["GET"])
def start():
    return redirect(url_for("index", table=db.addresses))

@app.route("/index/<table>", methods=["GET", "POST"])
def index(table):
    if request.method == "GET":

        table_columns = db.select_columns(table=db[table])
        table_columns_data = db.select_columns_data(db[table])

        #* Genera un formulario (clase) de FlaskWTF dinámicamente con las
        #* propiedades adecuadas por cada columna de la tabla. Este se
        #* insertará dentro del <modal>

        ModalForm = generate_dynamic_form(table_columns_data=table_columns_data, table_columns=table_columns, db=db)

        #* Instancia de la clase generada
        modal_form = ModalForm()

        return render_template('index.html',
                               table=table, tables=tables,
                               modal_form=modal_form), 200

    elif request.method == "POST":

        #* Para el llenado del <table> y el <modal>
        table_columns = db.select_columns(table=db[table])
        table_columns_data = db.select_columns_data(db[table])

        #* Genera un formulario (clase) de FlaskWTF dinámicamente con las
        #* propiedades adecuadas por cada columna de la tabla. Este se
        #* insertará dentro del <modal>

        ModalForm = generate_dynamic_form(table_columns_data=table_columns_data, table_columns=table_columns, db=db)

        #* Instancia de la clase generada
        modal_form = ModalForm(request.form)

        if modal_form.validate_on_submit():
            registry = {field.name: field.data for field in modal_form if
                        field.name != 'csrf_token' and field.name != 'submit'}

            db.insert_into(db[table], registry)

        return redirect(url_for("index", table=table))


@app.route("/index/<table>/<int:id>", methods=["DELETE", "PATCH"])
def delete(table, id):
    if request.method == "DELETE":
        if table in tables:
            db.delete_from(table=db[table], registry_id=id)
            return "Eliminación exitosa", 200

    elif request.method == "PATCH":
        if table in tables:
            pass

#* Rutas que devuelven información relevante en JSON.
#* Su uso radica solo para la renderización de la tabla.

@app.route("/data/<table>/body", methods=["GET"])
def body(table):
    table_body = db.select_all(table=db[table])
    table_body = [row._asdict() for row in table_body]
    return table_body


@app.route("/data/<table>/columns", methods=["GET"])
def columns(table):
    table_columns = db.select_columns(table=db[table])
    print(table_columns)
    return table_columns

