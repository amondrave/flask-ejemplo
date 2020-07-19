
from  app import db

class Usuario(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre_usuario = db.Column(db.String(50),index=True,nullable=False,unique=True)
    correo = db.Column(db.String(50),index=True,nullable=False,unique=True)
    contrasena = db.Column(db.String(100),nullable=False)

    def __init__(self,nombre_usuario,correo,contrasena):
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.contrasena = contrasena

    def __repr__(self):
         str = '<Usuario %r>' % self.nombre_usuario
