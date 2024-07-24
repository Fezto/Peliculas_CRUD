from re import findall

from wtforms.fields.datetime import DateField, TimeField  # <input type="datetime">
from wtforms.fields.numeric import IntegerField, DecimalField  # <input type="number">
from wtforms.fields.simple import StringField  # <input type="text">

from wtforms.validators import DataRequired, Length  # Validación del formulario

# * Define conjuntos de tipos de datos comunes en bases de datos que reciban
# * el mismo tratamiento genérico
float_types = ["FLOAT", "REAL", "DOUBLE PRECISION", "DECIMAL", "NUMERIC"]
date_types = ["DATE", "DATETIME"]


def generate_generic_field(column_data):

    column_name = column_data["name"]
    column_type = column_data["type"]

    if column_type == "INTEGER":
        return IntegerField(column_name, validators=[DataRequired()])
    elif any(float_type in column_type for float_type in float_types):
        return DecimalField(column_name, validators=[DataRequired()])
    elif any(date_type in column_type for date_type in date_types):
        return DateField(column_name, validators=[DataRequired()])
    elif column_type == "TIME":
        return TimeField(column_name, validators=[DataRequired()])
    else:
        # * Extraemos el número de VARCHAR para conseguir el límite
        numbers = findall(r'\d+', column_data["type"])
        if numbers:
            max_length = int(''.join(numbers))
            return StringField(column_name, validators=[DataRequired(), Length(max=max_length)])
        return StringField(column_name, validators=[DataRequired(), Length(max=0)])