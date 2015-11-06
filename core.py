#responder.py
import tweepy
from keys import *
from random import randint
from datetime import datetime,timedelta
import time
import os
import strings
## keys
#Twitter Keys


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


user = api.get_user(user_number)
#print(user.screen_name)
#print(user.followers_count)


class Scan_Trends:
    def scanner(self):
        trends= api.trends_place(2442047)
        hashtags= [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]

        trend_hashes= hashtags[0]
        #tweetSearch_results= api.search(q=trend_hashes,count= 50)

        return hashTags

class Follower:
    def __init__(self, twitterHandle):
        self.userName = twitterHandle
        self.followers = api.followers_ids(self.userName)
    def follower(self):
        counter = randint(0,100)
        for x in range(1):
            api.create_friendship(self.followers[counter])
            print("followed " + str(self.followers[counter]))
            counter -= 1
    def messager(self):
        numFollowers = len(self.followers)
        messageRecp = self.followers[random.randint(0,numFollowers)]
        msg = strings.replys[randint(0,len(strings.replys)-1)]
        api.send_direct_message(user_id = messageRecp, text = msg)

class Retweeter:
    def __init__(self):
        self.tweetList = []
    def retweetdump(self):
        self.searchQuery = strings.hashTags[randint(0,len(strings.hashTags)-1)]
        rand = randint(0,10)
        for result in api.search(q=self.searchQuery, lang="en"):
            self.tweetList.append(result.id)
        json.dump([self.tweetList], dump)
    def retweetSearch(self):
        self.searchQuery = strings.hashTags[randint(0,len(strings.hashTags)-1)]
        for result in api.search(q=self.searchQuery, lang="en"):
            self.tweetList.append(result.id)
        numTweets = len(self.tweetList)
        rand = randint(0,numTweets)
        api.retweet(self.tweetList[rand])
    def retweetFriends(self):
        numFollowers = len(ourAccount.followers)
        messageRecp = ourAccount.followers[random.randint(0,numFollowers)]
        for result in api.user_timeline(messageRecp):
            self.tweetList.append(result.id)
        numTweets = len(self.tweetList)
        rand = randint(0,numTweets)
        api.retweet(self.tweetList[rand])
    def retweeterRandom(self):
        rand = randint(0,1)
        if rand == 0:
            self.retweetSearch()
        else:
            self.retweetFriends()

class TweetBot:
    def __init__(self):
        self.tweetList1 = []
    def replyer(self):
        searchJunk = strings.hashTags[randint(0,len(strings.hashTags)-1)]
        self.searchQuery = searchJunk
        for result in api.search(q=self.searchQuery, lang="en"):
            self.tweetList1.append(result.id)
        time.sleep(2)
        numTweets = len(self.tweetList1)
        rand = randint(0,numTweets)
        tweetId = self.tweetList1[rand]
        user = api.get_status(tweetId)
        time.sleep(2)
        sn = user.user.screen_name
        msg = strings.replys[randint(0,len(strings.replys)-1)]
        content = "@{0}, {1} {2}".format(sn, msg, searchJunk)
        api.update_status(status=content, in_reply_to_status_id = tweetId)
        self.tweetList1 = []
    def tweeter(self):
        hashtag = strings.hashTags[randint(0,len(strings.hashTags)-1)]
        tweetMessage = strings.replys[randint(0,len(strings.replys)-1)]
        content = (tweetMessage + hashtag)
        print(content)
        api.update_status(status=content)
    def tweetChooser(self):
        probs = randint(1,100)
        if probs > 25:
            print('reply other', probs)
            self.replyer()
        else:
            print('tweet self', probs)
            self.tweeter()

class Core:
    def core(self):
        retweeter = Retweeter()
        scanTrends = Scan_Trends()
        justinFollower = Follower("justinbieber")
        userFollower = Follower("beliebthehype")
        tweetBot = TweetBot()
        print("starting?")
        while True:
            sleepy = randint(14400,21600)
            resty = randint(60,300)
            #the 15 mins twitter needs for clearing 429error
            resetTime = 900 
            probs = randint(1,1000)
            if probs < 100:
                #tweet canned message
                print("canned message")
                tweetBot.tweetChooser()
                time.sleep(resty)
            elif probs < 300:
                #look for followers
                try:
                    print('trying for followers')
                    #uncomment the one you want to use!
                    #justinFollower.follower()
                    #userFollower.follower()
                except:
                    print("timed out, passing")
                    time.sleep(resetTime)
                    pass
                print("look for followers")
                time.sleep(resty)
            elif probs < 400:
                #look to respond to top trending beiberTag
                try:
                    print("scanning trends")
                    scanTrends.scanner()
                except:
                    print("timed out, passing")
                    time.sleep(resetTime)
                    pass
                print("top trending")
                time.sleep(resty)
            elif probs < 900:
                #retweet a beiber related tweet
                try:
                    retweeter.retweeterRandom()
                    print("retweeted")
                except:
                    print("retweet failed, passing")
                    time.sleep(resetTime)
                time.sleep(resty)
            else:
                #go to bed
                print("sleep")

main = Core()
main.core()
