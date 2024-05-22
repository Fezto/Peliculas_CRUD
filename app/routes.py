from flask import render_template, url_for, flash
from app import app
from app.forms.login_form import LoginForm
from app.database import Database

db = Database()


@app.route("/index/<table>")
def index(table):
    table_headers = db.select_columns(table=db[table])
    table_body = db.select_all(table=db[table])
    return render_template('index.html', table_body=table_body, table_headers=table_headers)
