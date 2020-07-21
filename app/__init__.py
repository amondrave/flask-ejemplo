from .conexion import app
from .conexion import db
from app.models import models


#Creacion de la instancia de la base de datos

db.create_all()

# se importan las vistas de la aplicacion para que se tomen en cuenta
from app import views
from app import product_view

