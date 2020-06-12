from datetime import datetime
from models import Birthday
from app import db

def tweetBirthdays():
    birthdays = Birthday.query.filter_by(
        month = datetime.today().month,
        day = datetime.today().day
    ).all()

    for bd in birthdays:
        print(bd.first_name, bd.last_name, bd.day, bd.month, bd.year)

def addBirthday(first_name, last_name, day, month, year):
    bd = Birthday(first_name=first_name, last_name=last_name,
                    day=day, month=month, year=year
                 )
    db.session.add(bd)
    db.session.commit()
