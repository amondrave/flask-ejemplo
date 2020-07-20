from .conexion import app
from .conexion import db
from app.models import models


#Creacion del servidor

db.create_all()


from app import views
from app import product_view

