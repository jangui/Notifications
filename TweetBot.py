#!/usr/bin/env python3
import tweepy
from datetime import datetime, timedelta

class TweetBot():
    def __init__(self, keysFile):
        self.getKeys(keysFile)
        self.auth()

        ###deletion settings
        #minimum for likes required to keep
        self.keep_liked = 1
        #tweets containing these strings will not be deleted
        self.strings_to_keep = []
        #how old are tweets before deleting
        self.days_old = 2

    def getKeys(self, filename):
        self.keys = {}
        with open(filename, 'r') as f:
            for line in f:
                line = line.rstrip().split(" ")
                self.keys[line[0][:-1]] = line[1]


    def auth(self):
        auth = tweepy.OAuthHandler(self.keys["CONSUMER_KEY"],
                                   self.keys["CONSUMER_SECRET"])
        auth.set_access_token(self.keys["ACCESS_KEY"],
                              self.keys["ACCESS_SECRET"])
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(message)

    def delete_tweets(self):
        timeline = tweepy.Cursor(self.api.user_timeline).items()
        for tweet in timeline:
            #delete all tweets that dont pass check
            if (not self.keep_tweet(tweet)):
                self.api.destroy_status(tweet.id)

    # check if we want to keep tweet
    def keep_tweet(self, tweet):
        cutoff_date = datetime.utcnow() - timedelta(self.days_old)

        if tweet.favorite_count >= self.keep_liked:
            return True

        #if tweet has string in save list, keep
        for string in self.strings_to_keep:
            if tweet.text.find(string) > -1:
                return True

        #dont delete tweets younger than cutoff
        if tweet.created_at >= cutoff_date:
            return True

        return False
