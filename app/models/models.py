from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre_usuario = db.Column(db.String(50),index=True,nullable=False,unique=True)
    correo = db.Column(db.String(50),index=True,nullable=False,unique=True)
    contrasena = db.Column(db.String(100),nullable=False)

    def __str__(self):
            return "Usuario: {} ".format(self.nombre_usuario)

    def __repr__(self):
         return '<Usuario %r>' % self.nombre_usuario



class Producto(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    precio = db.Column(db.Float,nullable=False)

    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def retornar_productos(self):
        lista = []

        return  lista

    def __repr__(self):
        return '<Producto %r>' % self.nombre
