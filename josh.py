#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, sys, os
import time
from keys import *
import random
import json
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
dump = open('dump.txt', 'a+')
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
class Follower:
    def __init__(self, twitterHandle):
        self.userName = twitterHandle
        self.followers = api.followers_ids(self.userName)
    def follower(self):
        counter = random.randint(0,100)
        for x in range(1):
            api.create_friendship(self.followers[counter])
            print("followed " + str(self.followers[counter]))
            counter -= 1
    def messager(self):
        numFollowers = len(self.followers)
        messageRecp = self.followers[random.randint(0,numFollowers)]
        api.send_direct_message(user_id = messageRecp, text = "hi")
class Retweeter:
    def __init__(self):
        self.tweetList = []
    def retweetdump(self):
        self.searchQuery = str(input("Enter Search Term for retweet"))
        rand = random.randint(0,10)
        for result in api.search(q=self.searchQuery, lang="en"):
            self.tweetList.append(result.id)
        json.dump([self.tweetList], dump)
    def retweetSearch(self):
        self.searchQuery = str(input("Enter Search Term for retweet"))
        for result in api.search(q=self.searchQuery, lang="en"):
            self.tweetList.append(result.id)
        numTweets = len(self.tweetList)
        rand = random.randint(0,numTweets)
        api.retweet(self.tweetList[rand])
    def retweetFriends(self):
        numFollowers = len(ourAccount.followers)
        messageRecp = ourAccount.followers[random.randint(0,numFollowers)]
        for result in api.user_timeline(messageRecp):
            self.tweetList.append(result.id)
        numTweets = len(self.tweetList)
        rand = random.randint(0,numTweets)
        api.retweet(self.tweetList[rand])
    def retweeterRandom(self):
        rand = random.randint(0,1)
        if rand == 0:
            self.retweetSearch()
        else:
            self.retweetFriends()
ourAccount = Follower('beliebthehype')
justinBieber = Follower('justinbieber')
shit = Retweeter()
shit.retweeterRandom()






    