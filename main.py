import tweepy
import json
import re
import asyncio
import time
from textblob import TextBlob
from state_finder import statefinder, state_data
print(state_data)

with open('keys.json') as f_in:
	f_str = f_in.read()
	keys_dir = json.loads(f_str)

auth = tweepy.OAuthHandler(keys_dir['api_key'], keys_dir['api_secret_key'])
auth.set_access_token(keys_dir['access_token'], keys_dir['access_token_secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)

class Subject():
	def __init__(self, name):
		self.name = name
		self.sentamint = 0
		self.mentions = 0
		self.state_sentamint = {
			"AL": {"sentamint": 0, "mentions": 0},
			"AK": {"sentamint": 0, "mentions": 0},
			"AZ": {"sentamint": 0, "mentions": 0},
			"AR": {"sentamint": 0, "mentions": 0},
			"CA": {"sentamint": 0, "mentions": 0},
			"CO": {"sentamint": 0, "mentions": 0},
			"CT": {"sentamint": 0, "mentions": 0},
			"DE": {"sentamint": 0, "mentions": 0},
			"FL": {"sentamint": 0, "mentions": 0},
			"GA": {"sentamint": 0, "mentions": 0},
			"HI": {"sentamint": 0, "mentions": 0},
			"ID": {"sentamint": 0, "mentions": 0},
			"IL": {"sentamint": 0, "mentions": 0},
			"IN": {"sentamint": 0, "mentions": 0},
			"IA": {"sentamint": 0, "mentions": 0},
			"KS": {"sentamint": 0, "mentions": 0},
			"KY": {"sentamint": 0, "mentions": 0},
			"LA": {"sentamint": 0, "mentions": 0},
			"ME": {"sentamint": 0, "mentions": 0},
			"MD": {"sentamint": 0, "mentions": 0},
			"MA": {"sentamint": 0, "mentions": 0},
			"MI": {"sentamint": 0, "mentions": 0},
			"MN": {"sentamint": 0, "mentions": 0},
			"MS": {"sentamint": 0, "mentions": 0},
			"MO": {"sentamint": 0, "mentions": 0},
			"MT": {"sentamint": 0, "mentions": 0},
			"NE": {"sentamint": 0, "mentions": 0},
			"NV": {"sentamint": 0, "mentions": 0},
			"NH": {"sentamint": 0, "mentions": 0},
			"NJ": {"sentamint": 0, "mentions": 0},
			"NM": {"sentamint": 0, "mentions": 0},
			"NY": {"sentamint": 0, "mentions": 0},
			"NC": {"sentamint": 0, "mentions": 0},
			"ND": {"sentamint": 0, "mentions": 0},
			"OH": {"sentamint": 0, "mentions": 0},
			"OK": {"sentamint": 0, "mentions": 0},
			"OR": {"sentamint": 0, "mentions": 0},
			"PA": {"sentamint": 0, "mentions": 0},
			"RI": {"sentamint": 0, "mentions": 0},
			"SC": {"sentamint": 0, "mentions": 0},
			"SD": {"sentamint": 0, "mentions": 0},
			"TN": {"sentamint": 0, "mentions": 0},
			"TX": {"sentamint": 0, "mentions": 0},
			"UT": {"sentamint": 0, "mentions": 0},
			"VT": {"sentamint": 0, "mentions": 0},
			"VA": {"sentamint": 0, "mentions": 0},
			"WA": {"sentamint": 0, "mentions": 0},
			"WV": {"sentamint": 0, "mentions": 0},
			"WI": {"sentamint": 0, "mentions": 0},
			"WY": {"sentamint": 0, "mentions": 0}
		}

	def AddSentamint(self, sentamint, state):
		self.sentamint += sentamint
		self.mentions += 1
		if state != None:
			self.state_sentamint[state]['sentamint'] += sentamint
			self.state_sentamint[state]['mentions'] += 1
		
	
Trump = Subject('Trump')
Biden = Subject('Biden')


class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		for subject_person in [Trump, Biden]:
			if subject_person.name in status.text:
				Analysis = TextBlob(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", status.text).split()))					
				subject_person.AddSentamint(Analysis.sentiment.polarity, statefinder(status.user.location))


	def on_error(self, status_code):
		print(status_code)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['trump', 'biden'], is_async=True)

def divide(num1, num2):
	if num2 == 0:
		return 1
	else:
		return num1/num2

counter = 0
while True:
	for person in [Trump, Biden]:
		print('[{}]'.format(person.name))
		print("Sentiment (higher is better) "+str(person.sentamint))
		print("Mentioned "+str(person.mentions)+" times")
		
	print(str(counter*5)+' seconds since start')
	print(str(Trump.mentions + Biden.mentions)+" Tweets Analyzed")

	state_value = {
		"AL": 0,
		"AK": 0,
		"AZ": 0,
		"AR": 0,
		"CA": 0,
		"CO": 0,
		"CT": 0,
		"DE": 0,
		"FL": 0,
		"GA": 0,
		"HI": 0,
		"ID": 0,
		"IL": 0,
		"IN": 0,
		"IA": 0,
		"KS": 0,
		"KY": 0,
		"LA": 0,
		"ME": 0,
		"MD": 0,
		"MA": 0,
		"MI": 0,
		"MN": 0,
		"MS": 0,
		"MO": 0,
		"MT": 0,
		"NE": 0,
		"NV": 0,
		"NH": 0,
		"NJ": 0,
		"NM": 0,
		"NY": 0,
		"NC": 0,
		"ND": 0,
		"OH": 0,
		"OK": 0,
		"OR": 0,
		"PA": 0,
		"RI": 0,
		"SC": 0,
		"SD": 0,
		"TN": 0,
		"TX": 0,
		"UT": 0,
		"VT": 0,
		"VA": 0,
		"WA": 0,
		"WV": 0,
		"WI": 0,
		"WY": 0
	}
	for state_code in state_data.keys():
		trump_biden_support_ratio = divide(Trump.sentamint, Biden.sentamint)

		#Avg_Sentiment_trump = divide(Trump.state_sentamint[state_code]['sentamint'], Trump.state_sentamint[state_code]['mentions'])
		#Avg_Sentiment_biden = divide(Biden.state_sentamint[state_code]['sentamint'], Biden.state_sentamint[state_code]['mentions'])
		Sentiment_trump = Trump.state_sentamint[state_code]['sentamint'] / trump_biden_support_ratio
		Sentiment_biden = Biden.state_sentamint[state_code]['sentamint']
		how_republican = Sentiment_trump - Sentiment_biden
		state_value[state_code] = how_republican # The value is Page_View because it is from other code

	with open('state_values.js', 'w') as s_json:
		s_json.write("var j = "+json.dumps(state_value))
	time.sleep(5)
	counter += 1
