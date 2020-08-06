from flask import Flask, jsonify, request
from datetime import datetime

from .config import Config
from .utils import TweetBot

app = Flask(__name__)
app.config.from_object(Config())

KEYFILE = "/keys"
MAX_TWEET = 280

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

@app.route('/', methods=['POST'])
def tweetAPI():
    """
    function for tweeting
    tweet passed in payload. json must be in the form:
    {
        tweet: str
    }

    """
    payload = request.json
    if (payload['tweet']) == None:
        return "error: invalid payload, no tweet specified"
    ret = tweet(payload['tweet'])
    if ret[0] == False:
        return ret[1]
    return "success"

@app.route('/ping', methods=['GET'])
def ping():
    """
    hitting this endpoint will test tweet functionabilty
    """
    time = str(datetime.now())
    ret = tweet("PING " + time)
    if ret[0] == False:
        return ret[1]
    return "success"

@app.route('/delete', methods=['POST'])
def delete():
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
