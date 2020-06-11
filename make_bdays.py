from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)

class Birthday(db.Model):
    __tablename__ = 'birthday'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), index=True, nullable=False)
    last_name = db.Column(db.String(40), index=True)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer)



def getBirthdays(filename):
    bd = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip().split(" ")
            # lines that start with # are ignored
            name = [line[0]]
            if name[0][0] == "#":
                continue
            if line[1] != ".":
                name.append(" ".join(line[1:-1]))
            bd.append([name, line[-1].split("/")])
    return bd

birthdays = getBirthdays("birthdays")

for bd in birthdays:
    last_name = ''
    year = None
    first_name = bd[0][0]
    if len(bd[0]) > 1:
        last_name = bd[0][1:]
    day = bd[1][0]
    month = bd[1][1]
    if bd[1][2] != '0000':
        year = bd[1][2]
    bday = Birthday(first_name=first_name, last_name=last_name, day=day, month=month, year=year)
    db.session.add(bday)

db.session.commit()

