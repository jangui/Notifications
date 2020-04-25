#!/usr/bin/env python3
import tweepy

class TweetBot():
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.ACCESS_KEY = ACCESS_KEY
        self.ACCESS_SECRET = ACCESS_SECRET
        self.auth()

    def auth(self):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

    def tweet(self, message):
        self.api.update_status(message)
