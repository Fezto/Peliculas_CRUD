from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import IntegerField, DecimalField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired

from app.database import Database
from typing import List, Dict, Any


def generate_dynamic_form(table_columns_data: Dict[str, Any] = None, table_columns: List[str] = None, db: Database = None):
    print(type(table_columns_data))
    print(type(table_columns))
    return type('DynamicForm', (FlaskForm,), {
        column: get_field_class(table_columns_data[column], column, db) for column in table_columns
    })


def get_field_class(column_data, column, db):
    #* Si la columna tiene una llave foránea, crea un <select>
    if len(column_data["foreign_key"]) > 0:

        #* Para hacer la FK subscripteable
        foreign_keys = list(column_data["foreign_key"])

        #* Extraemos el nombre de la tabla referenciada
        foreign_table = foreign_keys[0].column.table.name
        foreign_table_body = db.select_all(db[foreign_table])

        choices = []

        print(foreign_table_body)
        for registry in foreign_table_body:
            choice_id = registry[0]
            choice_value = registry[1]
            choice = (choice_id, "id: " + str(choice_id) + " ("+ str(choice_value) + ")")
            choices.append(choice)

        return SelectField(column, choices=choices, validators=[DataRequired()])

    #* Si la columna no es una llave foránea, crea un <input> de acuerdo
    #* al tipo de dato de la columna dentro de la base de datos.
    elif "INTEGER" in column_data["type"]:
        return IntegerField(column, validators=[DataRequired()])
    elif any(
            float_type in column_data["type"] for float_type in ["FLOAT", "REAL", "DOUBLE PRECISION", "DECIMAL", "NUMERIC"]):
        return DecimalField(column, validators=[DataRequired()])
    elif any(date_type in column_data["type"] for date_type in ["DATE", "DATETIME"]):
        return DateField(column, validators=[DataRequired()])
    else:
        return StringField(column, validators=[DataRequired()])
