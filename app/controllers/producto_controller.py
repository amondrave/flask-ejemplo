from app import db
from app.models.models import Producto

class ProductoControlador:

    def crear_producto(self,producto):
        try:
            return True
        except:
            return False

    def eliminar_producto(self,producto_id):
        pass

    def retornar_producto(self,nombre):
        pass

