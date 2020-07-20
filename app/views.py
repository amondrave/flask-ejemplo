from app import app
from flask import request, render_template, redirect, url_for
from app.models.models import Usuario
from app.controllers.usuario_controller import UsuarioControlador

@app.route("/", methods=["GET","POST"])
def index():
    titulo = "login"
    if request.method == "POST":
        req = request.form
        nombre_usuario = req.get("username")
        correo = req.get("email")
        contrasena = req.get("password")
        print("los datos son: ",nombre_usuario,correo,contrasena)
        return  redirect(request.url)
    return render_template("public/index.html",titulo = titulo)
##Registro de usuarios en el sistema
# Pediremos los datos del formulario como se hizo en el metodo anterior
# Luego crearemos una instancia de la clase Usuario para la implementacion del metodo crear
# si todo sale bien se hara un @return a la vista del login
@app.route('/registro', methods=["GET","POST"])
def registro():
    titulo = "Registro"
    mensaje = "Bienvenido"
    if request.method == "POST":
        req = request.form
        nombre_usuario = req.get("username")
        correo = req.get("email")
        contrasena = req.get("password")
        print(nombre_usuario)
        print(contrasena)
        usuario = Usuario(nombre_usuario=nombre_usuario,correo=correo,contrasena=contrasena)
        usuario_controlador = UsuarioControlador(usuario)
        if usuario_controlador.agregar_usuario(usuario) == True:
            return redirect(url_for("index"))
        else:
            return redirect(url_for("error"))
    return render_template("public/registro.html",titulo=titulo, mensaje=mensaje)


@app.route("/error")
def error():
    return  render_template("public/error.html", alerta = "No se pudo agregar")

