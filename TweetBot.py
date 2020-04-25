#!/usr/bin/env python3
import tweepy

class TweetBot():
    def __init__(self, keysFile):
        self.getKeys(keysFile)
        self.auth()

    def getKeys(self, filename):
        self.keys = {}
        with open(filename, 'r') as f:
            lines = [line.rstrip().split(" ") for line in f]
            for line in lines:
                self.keys[line[0][:-1]] = line[1]

    def auth(self):
        callback_url = ''
        auth = tweepy.OAuthHandler(self.keys["CONSUMER_KEY"],
                                   self.keys["CONSUMER_SECRET"],
                                   callback_url)
        auth.set_access_token(self.keys["ACCESS_KEY"], self.keys["ACCESS_SECRET"])

        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(message)


t = TweetBot("keys")
