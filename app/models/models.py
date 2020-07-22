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
    tipo_producto = db.Column(db.Integer,db.ForeignKey('tipo.id'))
    def retornar_productos(self):
        lista = []

        return  lista

    def __repr__(self):
        return '<Producto %r>' % self.nombre
    def __str__(self):
        return "Producto: {} precio: {}".format(self.nombre,self.precio)


class Tipo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(70), index=True, unique=True)
    producto = db.relationship('Producto', backref = 'tipo', lazy = True )
    def __repr__(self):
        return "<Tipo %r>" % self.nombre

    def __str__(self):
        return "Tipo: {}".format(self.nombre)