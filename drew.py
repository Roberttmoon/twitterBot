from keys import *
import random
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class Autofav:
    def __init__(self):
        self.tweetList = [] #empty list

    def favSearch(self):
        self.searchQuery = str(input("Search for term"))
        for result in api.search(q=self.searchQuery, lang="en"):
            self.tweetList.append(result.id)
        numTweets = len(self.tweetList)
        rand = random.randint(0,numTweets) #adds tweets in a list, 0 to whatever
        api.create_favorite(self.tweetList[rand])

D = Autofav()# must set = to 
D.favSearch()

