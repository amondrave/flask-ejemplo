from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/discarok/Documentos/py-flask-env/base.db"
db = SQLAlchemy(app)

from app import views
from app import product_view