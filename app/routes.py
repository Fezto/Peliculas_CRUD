# ? Establece las rutas de nuestro servidor. Todas las peticiones de la página se
# ? redirigen aquí

from flask import render_template, url_for, request, redirect, jsonify
from sqlalchemy import inspect

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


# ! Ruta /index/<table> GET -> Su única función es la de actualizar el formulario
# ! con los <input> correspondientes al cambiar de tabla.
@app.route("/index/<table>", methods=["GET", "POST"])
def index(table):
    if request.method == "GET":
        if table in tables:
            # * Para el llenado del <table> y el <modal>
            table_columns = db.select_columns(table=db[table])
            table_columns_data = db.select_columns_data(db[table])

            # * Genera un formulario (clase) de FlaskWTF dinámicamente con las
            # * propiedades adecuadas por cada columna de la tabla. Este se
            # * insertará dentro del <modal>
            ModalForm = generate_dynamic_form(table_columns_data=table_columns_data, table_columns=table_columns, db=db)

            # * Instancia de la clase generada, el cual es un formulario genérico
            modal_form = ModalForm()

            return render_template('index.html', tables=tables,
                                   modal_form=modal_form), 200

    elif request.method == "POST":
        if table in tables:
            data = request.json
            data.pop("csrf_token", None)
            db.insert_into(table=db[table], data=data)
            return jsonify({"message": f"Registro con el id {id} actualizado con éxito"}), 200


@app.route("/index/<table>/<int:id>", methods=["DELETE", "PUT"])
def delete(table, id):
    if request.method == "DELETE":
        if table in tables:
            db.delete_from(table=db[table], registry_id=id)
            return jsonify({"message": f"Registro con el id {id} eliminado con éxito"}), 200

    elif request.method == "PUT":
        if table in tables:
            data = request.json
            data.pop("csrf_token", None)
            db.update_from(table=db[table], data=data, registry_id=id)
            return jsonify({"message": f"Registro con el id {id} actualizado con éxito"}), 200


# * Rutas que devuelven información relevante en JSON.
# * Su uso radica solo para la renderización de la tabla.


@app.route("/data/<table>/columns", methods=["GET"])
def columns(table):
    table_columns = db.select_columns(table=db[table])
    print(table_columns)
    return table_columns

@app.route("/data/<table>/<int:id>", methods=["GET"])
def registry(table, id):
    registry = db.select_all(table=db[table], registry_id=id)
    registry = registry._asdict()
    return registry

@app.route("/data/<table>/body", methods=["GET"])
def body(table):
    table_body = db.select_all(table=db[table])
    table_body = [row._asdict() for row in table_body]

    # Diccionarios para mapear IDs a nombres en las tablas referenciadas
    reference_data = {
        "peliculas": db.select_all(table=db["peliculas"]),
        "salas": db.select_all(table=db["salas"]),
        "generos": db.select_all(table=db["generos"]),
        "clasificaciones": db.select_all(table=db["clasificaciones"]),
        "tipo_salas": db.select_all(table=db["tipo_salas"]),
        "clientes": db.select_all(table=db["clientes"]),
        "funciones": db.select_all(table=db["funciones"])
    }

    # Crear diccionarios para mapear IDs a nombres
    reference_dicts = {
        "peliculas": {item.id: item.titulo for item in reference_data["peliculas"]},
        "salas": {item.id: item.id for item in reference_data["salas"]},
        "generos": {item.id: item.genero for item in reference_data["generos"]},
        "clasificaciones": {item.id: item.clasificacion for item in reference_data["clasificaciones"]},
        "tipo_salas": {item.id: item.nombre for item in reference_data["tipo_salas"]},
        "clientes": {item.id: item.nombre for item in reference_data["clientes"]},
        "funciones": {item.id: item.fecha for item in reference_data["funciones"]}
    }

    # Reemplazar los IDs foráneos con sus nombres correspondientes
    for row in table_body:
        if table == "funciones":
            row["pelicula_id"] = reference_dicts["peliculas"].get(row["pelicula_id"], "Desconocido")
            row["sala_id"] = reference_dicts["salas"].get(row["sala_id"], "Desconocido")
        elif table == "peliculas":
            row["genero_id"] = reference_dicts["generos"].get(row["genero_id"], "Desconocido")
            row["clasificacion_id"] = reference_dicts["clasificaciones"].get(row["clasificacion_id"], "Desconocido")
        elif table == "salas":
            row["tipo_sala_id"] = reference_dicts["tipo_salas"].get(row["tipo_sala_id"], "Desconocido")
        elif table == "reservas":
            row["cliente_id"] = reference_dicts["clientes"].get(row["cliente_id"], "Desconocido")
            row["funcion_id"] = reference_dicts["funciones"].get(row["funcion_id"], "Desconocido")

    return jsonify(table_body)

