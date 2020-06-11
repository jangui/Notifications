from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)

class Birthday(db.Model):
    def __init__(**kwargs):
        super(Birthday, self).__init__(**kwargs)

    __tablename__ = 'birthday'
    first_name = db.Column(db.String(15), index=True, nullable=False, primary_key=True)
    last_name = db.Column(db.String(40), index=True, default='', primary_key= True)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer)

db.create_all()
