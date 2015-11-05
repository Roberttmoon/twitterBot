import tweepy, random, time
from keys import *

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api= tweepy.API(auth)

class Scan_Trends:
	# consumer_key= keys['consumer_key']
	# consumer_secret= keys['consumer_secret']
	# access_token= keys['access_token']
	# access_token_secret= keys['access_token_secret']
	def scanner(self):
		while True:
			trends= api.trends_place(2442047)
			hashtags= [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]

			trend_hashes= hashtags[0]
			tweetSearch_results= api.search(q=trend_hashes, count= 50)
			print(hashtags)
	sleepy_time= random.randint(120, 360)
	time.sleep(sleepy_time)

zergle= Scan_Trends()
zergle.scanner()