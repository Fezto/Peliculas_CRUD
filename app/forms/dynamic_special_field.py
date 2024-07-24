import phonenumbers
from wtforms.fields.simple import EmailField, StringField
from wtforms.validators import Email, ValidationError


def generate_special_field(column_data):
    column_name = column_data["name"]

    if column_name == "correo":
        return EmailField(column_name, validators=[Email()])

    if column_name == "telefono":
        return StringField(column_name, validators=[Email(), validate_phone])

def validate_phone(form, field):
    try:
        input_number = phonenumbers.parse(field.data, None)
        if not phonenumbers.is_valid_number(input_number):
            raise ValidationError('Invalid phone number.')
    except Exception as e:
        raise ValidationError('Invalid phone number format. Please include country code.')


