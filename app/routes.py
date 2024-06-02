from flask import render_template, url_for, flash, send_from_directory, request, redirect

from app import app
from app.database import Database
from app.forms.modal_form import generate_dynamic_form

#* Instancia para el contacto con nuestra base de datos
db = Database()

#* Para llenar las opciones en el <navbar> lateral
tables = db.select_tables()


@app.route("/", methods=["GET"])
def start():
    return redirect(url_for("index", table=db.addresses))


@app.route("/index/<table>", methods=["GET", "POST"])
def index(table):
    if request.method == "GET":

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

        return render_template('index.html',
                               table=table, table_body=table_body, table_headers=table_columns, tables=tables,
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


