from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "hello world"
