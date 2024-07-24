# ? Función que se encarga de generar una clase de FlaskWTF con los <input>
# ? y <select> correctos de acorde a las necesidades de cada tabla

from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField  # <input type="button">

from app.database import Database

from typing import List, Dict, Any  # Validación de datos y documentación

from app.forms.dynamic_select_field import generate_select_field
from app.forms.dynamic_generic_field import generate_generic_field
from app.forms.dynamic_special_field import generate_special_field


# * Define el nombre de las columnas/campos que requerirán un tratamiento especial.
special_fields = ["correo", "telefono", "numero_sala"]

# * Función que genera clases (formularios de Flask-WTF genéricos) dinámicamente.
def generate_dynamic_form(table_columns_data: Dict[str, Any], table_columns: List[str],
                          db: Database):
    # * Los <input> dependerán del tipo de columna.
    fields = {column: get_field_class(table_columns_data[column], db) for column in table_columns[1:]}
    fields['submit'] = SubmitField("Insertar")
    return type("DynamicForm", (FlaskForm,), fields)


# * Define si cada columna debe de recibir datos por un <input> o un <select>.
# * En caso de ser por un <input>, tambien define cuál tipo.
def get_field_class(column_data, db):
    # * Obtenemos los nombres de las columnas de la tabla a tratar.
    column_names = [column_data["name"] for _ in column_data]

    # * Si la columna tiene una llave foránea, crea un <select>
    # * Es necesario pasar a db debido a que necesitamos consultar información
    # * de una tabla ajena.
    if len(column_data["foreign_key"]) > 0:
        return generate_select_field(column_data, db)

    # * Si la columna requiere un tratamento especial, tratarlo como tal.
    elif any(special_field in column_names for special_field in special_fields):
        print("Columna especial detectada:", column_data["name"])
        return generate_special_field(column_data)

    # * En caso de que se requiera un campo genérico, aplicarlo.
    else:
        return generate_generic_field(column_data)



