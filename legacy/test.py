import tweepy
import json
import re
import asyncio
import time
from textblob import TextBlob
from state_finder import statefinder, state_data

with open('keys.json') as f_in:
	f_str = f_in.read()
	keys_dir = json.loads(f_str)

auth = tweepy.OAuthHandler(keys_dir['api_key'], keys_dir['api_secret_key'])
auth.set_access_token(keys_dir['access_token'], keys_dir['access_token_secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)


		
	
Trump = {"name": "Trump", "sentamint": 0, "mentions": 0, "state_sentamint": state_data}
Biden = {"name": "Biden", "sentamint": 0, "mentions": 0, "state_sentamint": state_data}

def AddSentamint(person, sentamint, state):
	person['sentamint'] += sentamint
	person['mentions'] += 1
	if state != None:
		person['state_sentamint'][state]['sentamint'] += sentamint
		person['state_sentamint'][state]['mentions'] += 1

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):

				
		if Biden['name'] in status.text:
			Analysis = TextBlob(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", status.text).split()))
			state = statefinder(status.user.location)
			if state == 'CA' and Analysis.sentiment.polarity != 0:
				print(Biden['name'])
				
			AddSentamint(Biden, Analysis.sentiment.polarity, state)


	def on_error(self, status_code):
		print(status_code)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['trump', 'biden'])

counter = 0
counter = 0
while True:
	for person in [Trump, Biden]:
		print('[{}]'.format(person['name']))
		print("sentamint (higher is better) "+str(person['sentamint']))
		print("mentioned "+str(person['mentions'])+" times")
		
	print(str(counter*5)+' seconds since start')
	print(str(Trump.mentions + Biden.mentions)+" Tweets Analyzed")
	time.sleep(5)
	counter += 1