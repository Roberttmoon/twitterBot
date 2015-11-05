#responder.py
import tweepy
from keys import *
from random import randint

## keys
#Twitter Keys


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


user = api.get_user(user_number)
#print(user.screen_name)
#print(user.followers_count)

class ResponceMachine:
    follows = None
    message = None
    def __init__(self, hashtag):
        self.hashtag = hashtag
    def followerChecker(self):
        follows = user.followers_count
        if follows > 50:
            return self.beiberHate()
        else:
            return self.beiberLove()
    def beiberHate(self):
        with open('beiberHate.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
            print(message)
            return message
    def beiberLove(self):
        with open('beiberLove.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
            print(message)
            return message



hashtag = "#hastag"
responder = ResponceMachine(hashtag)
responder.followerChecker()