#!/usr/bin/env python3
from birthdays import tweetBirthdays
"""
Place for daily tasks to be executed
"""
keyfile = "my_keys"
bdayfile = "birthdays"

def main():
    tweetBirthdays(keyfile, bdayfile)

if __name__ == "__main__":
    main()

