import tweepy
from keys import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trend = (api.trends_place(2379574))
print(trend)