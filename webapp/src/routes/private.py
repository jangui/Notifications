from flask import Blueprint, jsonify, request
from ..utils import get_birthdays, TweetBot, add_birthday, update_birthday, delete_birthday
from datetime import datetime

private = Blueprint('private', __name__, url_prefix='/private')

@private.route('/tweet/birthdays', methods=['POST'])
def tweet_birthdays():
    keyfile = "../data/keys"
    bds = get_birthdays()
    bot = TweetBot(keyfile)
    for key, value in bds.items():
        twt = "Today is " + key + "'s birithday!"
        if value != '':
            twt += " (" + str(value) + ")"
        bot.tweet(twt)
    return jsonify(bds)

@private.route('/tweet/ping', methods=['POST'])
def ping():
    print(request.json)
    time = str(datetime.now())
    keyfile = "../data/keys"
    bot = TweetBot(keyfile)
    bot.tweet("PING " + time)
    return "success!"

@private.route('/tweet/delete', methods=['POST'])
def delete():
    keyfile = "../data/keys"
    bot = TweetBot(keyfile)
    bot.delete_tweets()
    return "success!"

@private.route('/birthdays/add', methods=['POST'])
def add_bd():
    """
    payload should be json in the form:
    {
        first_name: str
        last_name: str (omit last name using empty string)
        day: int
        month: int
        year: int (omit birth year using -1)
    }

    """
    payload = request.json
    print(payload)
    if payload['year'] == "":
        payload['year'] = None
    add_birthday(
                    payload['first_name'],
                    payload['last_name'],
                    payload['day'],
                    payload['month'],
                    payload['year']
                )
    return 'succes!'


@private.route('/birthdays/delete', methods=['POST'])
def delete_bd():
    """
    payload should be json in the form:
    {
        first_name: str
        last_name: str
    }
    """
    payload = request.json
    delete_birthday(payload['first_name'], payload['last_name'])
    return 'success!'

@private.route('/birthdays/update', methods=['POST'])
def update_bd():
    """
    payload should be json in the form:
    {
        first_name: str
        last_name: str (omit last name using empty string)
        day: int
        month: int
        year: int (omit birth year using empty string)
    }

    """
    payload = request.json
    if payload['year'] == "":
        payload['year'] = None
    update_birthday(
                        payload['first_name'],
                        payload['last_name'],
                        payload['day'],
                        payload['month'],
                        payload['year']
                    )
    return 'success!'
