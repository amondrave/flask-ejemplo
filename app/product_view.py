from  app import app
from flask import render_template

@app.route("/productos")
def obtener_productos():
    usuario = "Angel"
    return render_template("product/inicio.html",usuario = usuario)