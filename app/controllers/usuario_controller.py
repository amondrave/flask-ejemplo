from app import db
from app.models.models import Usuario

class UsuarioControlador:

    def __init__(self, usuario):
        self.usuario = usuario

    def agregar_usuario(self,usuario):
        try:            
            db.session.add(usuario)
            db.session.commit()
            return True
        except:
            print(usuario)
            print("Algo salio mal")        
            return False

    # Metodo que me ayuda a determinar que el usuario exista en el sistema
    # Pide el nombre de usuario para asegurarse de que este se encuentre registrado
    # Luego compara si el correo y la contraseña corresponda a este para retornar verdadero
    def existe_usuario(self, nombre_usuario,correo,contrasena):
        try:
            usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()
            if usuario is not None:
                if usuario.correo == correo and usuario.contrasena == contrasena:
                    return True
                else:
                    print("Datos incorrectos")
                    return False
            else:
                print("El usuario no existe")
                return False
        except:
            print("Fallo en el intento de recuperar la info")
            return False

    def listar_usuarios(self):
        try:
            lista = Usuario.query.all()
            return lista
        except:
            return []

    #Metodo para buscar un usuario por id
    def buscar_usuario_id(self, id):
        try:
            usuario = Usuario.query.filter_by(id=id).first()
            return usuario
        except:
            return None