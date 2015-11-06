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

class FileHandler:
    def hashTagsList(self):
        with open('hashTags.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
            return message
    def cannedTweetsPositve(self):
        with open('beiberLove.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
            return message
        print('hai <3')
    def cannedTweetsNegitive(self):
        with open('beiberHate.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
            return message
        print('fuckoff')
    def dumpTruckGetter(self):
        with open('dump.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
            return message


class ResponceMachine:
    follows = None
    message = None
    def __init__(self):
        self.fileHandler = FileHandler()
    def followerChecker(self):
        follows = user.followers_count
        print(follows)
        if follows > 300:
            return self.beiberHate()
        else:
            return self.beiberLove()
    def beiberHate(self):
        message = self.fileHandler.cannedTweetsNegitive()
        print(message)
        return message
    def beiberLove(self):
        message = self.fileHandler.cannedTweetsPositve()
        print(message)
        return message



class Main:
    def main(self):
        fileHandler = FileHandler()
        responceMachine = ResponceMachine()
        responceMachine.followerChecker()

mainy= Main()
mainy.main()
