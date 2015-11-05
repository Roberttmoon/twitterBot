#responder.py
import tweepy
from keys import *
from random import randint
from datetime import datetime,timedelta
import time
import os
## keys
#Twitter Keys


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


user = api.get_user(user_number)
#print(user.screen_name)
#print(user.followers_count)

class FileHandler:
    def hashTagsList(slef):
        with open('hashTags.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
    def cannedTweetsPositve(self):
        with open('beiberLove.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
    def cannedTweetsNegitive(self):
        with open('beiberHate.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()
    def dumpTruckGetter(self):
        with open('dump.txt','r') as f:
            lines = f.read().splitlines()
            message = lines[randint(0,len(lines)-1)]
            f.close()


class Scan_Trends:
    files = FileHandler()
    def scanner(self):
        trends= api.trends_place(2442047)
        hashtags= [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]

        trend_hashes= hashtags[0]
        #tweetSearch_results= api.search(q=trend_hashes,count= 50)

        return hashTags
            
class ResponceMachine:
    files = FileHandler()
    follows = None
    message = None
    def __init__(self):
        pass
    def followerChecker(self):
        follows = user.followers_count
        if follows > 300:
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


class FollowerGenerator:
    files = FileHandler()
    def __init__(self):
        self.userName = str(input("Enter Username"))
    def followerFinder(self):
        self.followers = api.followers_ids(self.userName)
    def follower(self):
        counter = random.randint(0,100)
        for x in range(1):
            api.create_friendship(self.followers[counter])
            print("followed " + str(self.followers[counter]))
            counter -= 1

class Retweeter:
    files = FileHandler()
    def __init__(self):
        self.dumptruck = []
        self.searchQuery = str(input("Enter Search Term for retweet"))
    def retweet(self):
        rand = random.randint(0,10)
        for result in api.search(q=self.searchQuery, lang="en"):
            self.dumptruck.append(result.id)
        api.retweet(self.dumptruck[rand])
    # def retweeter():
    #     retweetDude = Retweeter()
    #     retweetDude.retweet()

class Core:
    files = FileHandler()
    def core(self):
        responceMachine = ResponceMachine()
        retweeter = Retweeter()
        scanTrends = Scan_Trends()
        followerGen = FollowerGenerator
        while True:
            sleepy = randint(14400,21600)
            resty = randint(60,300)
            #the 15 mins twitter needs for clearing 429error
            resetTime = 900 
            probs = randint(1,1000)
            if probs < 100:
                #tweet canned message
                responceMachine.followerChecker()
                print("canned message")
                time.sleep(resty)
            elif probs < 300:
                #look for followers
                try:
                    followDude.followerFinder()
                    followDude.follower()
                except:
                    time.sleep(resetTime)
                    print("timed out, passing")
                    pass
                print("look for followers")
                time.sleep(resty)
            elif probs < 400:
                #look to respond to top trending beiberTag
                try:
                    scanTrends.scanner()
                except:
                    time.sleep(resetTime)
                    print("timed out, passing")
                    pass
                print("top trending")
                time.sleep(resty)
            elif probs < 900:
                #retweet a beiber related tweet
                try:
                    retweeter.retweet()
                    print("retweeted")
                except:
                    print("retweet failed, passing")
                    pass
                    time.sleep(resetTime)
                time.sleep(resty)
            else:
                #go to bed
                print("sleep")

main = Core()
main.core()