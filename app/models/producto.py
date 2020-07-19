from app import db

class Producto(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
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