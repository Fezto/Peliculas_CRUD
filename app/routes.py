# ? Establece las rutas de nuestro servidor. Todas las peticiones de la página se
# ? redirigen aquí

from flask import render_template, url_for, request, redirect, jsonify

from app import app
from app.database import Database
from app.forms.modal_form import generate_dynamic_form

# * Instancia para el contacto con nuestra base de datos
db = Database()

# * Para llenar las opciones en el <navbar> lateral
tables = db.select_tables()


# * Rutas principales. Estas son las que responden ante las solicitudes HTTP
# * del cliente.


# ! Ruta raíz -> Redirige a la primer tabla de la DB
@app.route("/", methods=["GET"])
def start():
    return redirect(url_for("index", table=db[tables[0]]))


# ! Ruta /index/<table> -> Su única función es la de actualizar el formulario
# ! con los <input> correspondientes al cambiar de tabla.
@app.route("/index/<table>", methods=["GET", "POST"])
def index(table):
    if request.method == "GET":
        print("tabla actual: ", table)
        table_columns = db.select_columns(table=db[table])
        table_columns_data = db.select_columns_data(db[table])

        # * Genera un formulario (clase) de FlaskWTF dinámicamente con las
        # * propiedades adecuadas por cada columna de la tabla. Este se
        # * insertará dentro del <modal>

        ModalForm = generate_dynamic_form(table_columns_data=table_columns_data, table_columns=table_columns, db=db)

        # * Instancia de la clase generada
        modal_form = ModalForm()

        return render_template('index.html', tables=tables,
                               modal_form=modal_form), 200

    elif request.method == "POST":
        # * Para el llenado del <table> y el <modal>
        table_columns = db.select_columns(table=db[table])
        table_columns_data = db.select_columns_data(db[table])

        # * Genera un formulario (clase) de FlaskWTF dinámicamente con las
        # * propiedades adecuadas por cada columna de la tabla. Este se
        # * insertará dentro del <modal>

        ModalForm = generate_dynamic_form(table_columns_data=table_columns_data, table_columns=table_columns, db=db)

        # * Instancia de la clase generada
        modal_form = ModalForm(request.form)

        if modal_form.validate_on_submit():
            registry = {field.name: field.data for field in modal_form if
                        field.name != 'csrf_token' and field.name != 'submit'}

            db.insert_into(table=db[table], data=registry)
            return jsonify({'message': 'Registry added successfully'}), 200

        return jsonify({'message': 'Invalid form data'}), 400


@app.route("/index/<table>/<int:id>", methods=["DELETE", "PUT"])
def delete(table, id):
    if request.method == "DELETE":
        if table in tables:
            db.delete_from(table=db[table], registry_id=id)
            return jsonify({"message": "Successful deletion"}), 200

    elif request.method == "PUT":
        if table in tables:
            data = request.json
            data.pop("csrf_token", None)
            db.update_from(table=db[table], data=data, registry_id=id)
            return jsonify({"message": "Successful update"}), 200


# * Rutas que devuelven información relevante en JSON.
# * Su uso radica solo para la renderización de la tabla.

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
