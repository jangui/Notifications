from TweetBot import TweetBot
from datetime import datetime

def tweetBirthdays(keyfile, bdayfile):
    t = TweetBot(keyfile)
    birthdays = getBirthdays(bdayfile)
    for k, v in birthdays.items():
        if v[2] == "0000":
            age = None
            y = datetime.today().year
        else:
            y = int(v[2])
            age = datetime.today().year - y
        m = int(v[1])
        d = int(v[0])
        dt = datetime(y,m,d)
        if (dt.month == datetime.today().month
           and dt.day == datetime.today().day):
            msg = "Today is " + k + "'s birthday!"
            if age:
                msg += " (" + str(age) + ")"
            t.tweet(msg)

def getBirthdays(filename):
    bd = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip().split(" ")
            name = line[0]
            # lines that start with # are ignored
            if name[0] == "#":
                continue
            if line[1] != ".":
                name += " " + line[1]
            bd[name] = line[2].split("/")
    return bd
