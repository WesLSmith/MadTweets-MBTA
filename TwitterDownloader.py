from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

access_token = "x"
access_token_secret = "x"
consumer_key = "x"
consumer_secret = "x"

# file name that you want to open is the second argument
save_file = open('data.json', 'a')

class listener(StreamListener):

    def on_data(self, data):       
        with open('fetched_tweets.txt','a') as textfile:
            textfile.write(data)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["mbta","MBTA"])