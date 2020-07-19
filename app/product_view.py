from  app import app

@app.route("/productos")
def obtener_productos():
    return "<h1>Esta se la la lista de productos que están en el sistema</h1>"