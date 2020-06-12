from datetime import datetime
from ..app import db
from ..models import Birthday

def get_birthdays():
    """
    Queries database for people with a birthday on today's date
    Returns dictionary where name is key and age is value
    """
    birthdays = Birthday.query.filter_by(
        month = datetime.today().month,
        day = datetime.today().day
    ).all()

    bds = {}
    for bd in birthdays:
        name = bd.first_name
        if bd.last_name != '':
            name += bd.last_name
        if not bd.year:
            age = ''
        else:
            age = datetime.today().year - bd.year
        bds[name] = age
    return bds;

def add_birthday(first_name, last_name, day, month, year):
    bd = Birthday(first_name=first_name, last_name=last_name,
                    day=day, month=month, year=year
                 )
    db.session.add(bd)
    db.session.commit()
