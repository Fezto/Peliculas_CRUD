from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired


def generate_select_field(column_data, db):

    column_name = column_data["name"]

    # * Para hacer la FK subscripteable
    foreign_keys = list(column_data["foreign_key"])

    # * Extraemos el nombre de la tabla referenciada y su contenido
    foreign_table = foreign_keys[0].column.table.name
    foreign_table_body = db.select_all(db[foreign_table])

    # * Las elecciones que tendrá el usuario en el <select>
    choices = []

    for registry in foreign_table_body:
        choice_value = registry[0]  # ? El valor "real" a subir en el form será el id
        choice_show_name = registry[1]  # ? El nombre o valor con el que se muestra en front
        choice = (choice_value, choice_show_name)
        choices.append(choice)

    return SelectField(column_name, choices=choices, validators=[DataRequired()])