from flask import render_template, url_for, flash, send_from_directory, request
from app import app
from app.forms.login_form import LoginForm
from app.database import Database

db = Database()


@app.route("/index/<table>", methods=["GET", "POST"])
def index(table):
    if request.method == "GET":
        table_headers = db.select_columns(table=db[table])
        table_body = db.select_all(table=db[table])
        tables = db.select_tables()
        db.insert_into(db.materials, {"name_material": "Arena2"})

        return render_template('index.html', table_body=table_body, table_headers=table_headers, tables=tables)

