#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, sys, os
import time
from keys import *
import random
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
class FollowerGenerator:
    def __init__(self):
        self.userName = str(input("Enter Username"))
    def followerFinder(self):
        self.followers = api.followers_ids(self.userName)
    def follower(self):
        counter = 0
        for x in self.followers:
            api.create_friendship(self.followers[counter])
            print("followed " + str(self.followers[counter]))
            counter += 1
    def followerGenerator():
        followDude = FollowerGenerator()
        followDude.followerFinder()
        followDude.follower()
class Retweeter:
    def __init__(self):
        self.dumptruck = []
        self.searchQuery = str(input("Enter Search Term for retweet"))
    def retweet(self):
        rand = random.randint(0,10)
        for result in api.search(q=self.searchQuery, lang="en"):
            self.dumptruck.append(result.id)
        api.retweet(self.dumptruck[rand])
    def retweeter():
        retweetDude = Retweeter()
        retweetDude.retweet()

    