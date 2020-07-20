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

