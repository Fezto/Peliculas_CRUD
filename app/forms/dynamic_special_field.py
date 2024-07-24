from wtforms.fields.choices import SelectField
from wtforms.fields.simple import EmailField
from wtforms.validators import Email, DataRequired, Length
from wtforms.fields import TelField


def generate_special_field(column_data):
    column_name = column_data["name"]

    if column_name == "correo":
        email_regex = ".+@(gmail|yahoo|hotmail|outlook)\\.(com|net|edu)"
        return EmailField(column_name, validators=[DataRequired(), Email()], render_kw={"pattern": email_regex})

    if column_name == "telefono":
        tel_regex = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
        return TelField(column_name, validators=[DataRequired(), Length(min=10, max=15)],
                        render_kw={"pattern": tel_regex, "placeholder": "442-194-1607"})

    if column_name == "numero_sala":
        tipo_sala_choices = [(i, str(i)) for i in range(1, 15)]
        return SelectField(column_name, choices=tipo_sala_choices)
