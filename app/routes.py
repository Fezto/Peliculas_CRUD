from flask import render_template, url_for, flash
from app import app
from app.forms.login_form import LoginForm


@app.route("/")
@app.route("/index")
def index():
    login_form = LoginForm()
    return render_template('index.html', login_form=login_form)

@app.route("/db")
def db():
