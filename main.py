import tweepy

import json

with open('keys.json') as f_in:
	keys_dir = json.load(f_in)


auth = tweepy.OAuthHandler(keys_dir['api_key'], keys_dir['api_secret_key'])
auth.set_access_token(keys_dir['access_token'], keys_dir['access_token_secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)



class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['python'], is_async=True)
