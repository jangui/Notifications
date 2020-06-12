from flask import Blueprint, jsonify
from ..utils import get_birthdays, TweetBot
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

