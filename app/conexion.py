from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/chus/Documentos/Portafolio/flask/flask-ejemplo/base.db"
db = SQLAlchemy(app)
