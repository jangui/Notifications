#!/usr/bin/env python3
from TweetBot import TweetBot
from birthdays import tweetBirthdays
"""
Place for daily tasks to be executed
"""
keyfile = "my_keys"
bdayfile = "birthdays"

def main():
    bot = TweetBot(keyfile)
    bot.delete_tweets()
    tweetBirthdays(bot, bdayfile)

if __name__ == "__main__":
    main()

