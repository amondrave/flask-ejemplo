from app import app
from flask import request, render_template

@app.route("/")
def index():
    titulo = "login"
    return render_template("public/index.html")
@app.route('/registro')
def registro():
    return "Este sera el registro de usuarios"


