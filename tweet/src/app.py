from flask import Flask, jsonify, request
from datetime import datetime
from os import getenv

from .config import Config
from .utils import TweetBot

app = Flask(__name__)
app.config.from_object(Config())

MAX_TWEET = int(getenv("MAX_TWEET"))
TOKEN = getenv("TOKEN")
KEYFILE = "/keys"

def tweet(twt):
    if len(twt) > MAX_TWEET:
        err = "error: tweet (length: "+str(len(twt))+") "
        err += "exceedes limit ("+str(MAX_TWEET)+")"
        return (False, err)
    bot = TweetBot()

    #get api keys from file
    ret = bot.getKeys(KEYFILE)
    if (ret[0] == False):
        return ret

    #authenticate keys
    ret = bot.auth()
    if (ret[0] == False):
        return ret

    #tweet
    ret = bot.tweet(twt)
    return ret

@app.route('/', methods=['GET', 'POST'])
def tweetAPI():
    """
    function for tweeting
    tweet passed in payload. json must be in the form:
    {
        tweet: str
    }

    """
    payload = request.json
    if payload == None or 'token' not in payload.keys():
        return "404 page not found" #purposely unambiguous
    if payload['token'] != TOKEN:
        return "invalid token"

    if payload['tweet'] == None:
        return "error: invalid payload, no tweet specified"

    ret = tweet(payload['tweet'])
    if ret[0] == False:
        return ret[1]
    return "success"

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    """
    hitting this endpoint will test tweet functionabilty
    """
    if payload == None or 'token' not in payload.keys():
        return "404 page not found" #purposely unambiguous
    if payload['token'] != TOKEN:
        return "invalid token"

    time = str(datetime.now())
    ret = tweet("PING " + time)
    if ret[0] == False:
        return ret[1]
    return "success"

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if payload == None or 'token' not in payload.keys():
        return "404 page not found" #purposely unambiguous
    if payload['token'] != TOKEN:
        return "invalid token"

    bot = TweetBot()

    #get api keys from file
    ret = bot.getKeys(KEYFILE)
    if (ret[0] == False):
        return ret

    #authenticate keys
    ret = bot.auth()
    if (ret[0] == False):
        return ret

    #delete tweets
    ret = bot.delete_tweets()
    if ret[0] == False:
        return ret[1]
    return "success"
