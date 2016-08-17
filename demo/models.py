from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


class Cupcakes(db.Model):
    __tablename__ = 'cupcakes'
    id = db.Column(db.Integer, primary_key=True)
    delicious = db.Column(db.Boolean)
    quantity = db.Column(db.Integer)



