from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    last_name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Constraseña", validators=[DataRequired()])