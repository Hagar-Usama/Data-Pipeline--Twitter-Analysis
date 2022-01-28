import boto3
import random
import time
import json
import random

# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream
from configparser import ConfigParser

parser = ConfigParser()
parser.read('api_auth.cfg')

# This is the super secret information that will allow access to the Twitter API and AWS Comprehend
# access_token = parser.get('api_tracker', 'access_token')
# access_token_secret = parser.get('api_tracker', 'access_token_secret')
# consumer_key = parser.get('api_tracker', 'consumer_key')
# consumer_secret = parser.get('api_tracker', 'consumer_secret')
aws_key_id = parser.get('api_tracker', 'aws_key_id')
aws_key = parser.get('api_tracker', 'aws_key')

DeliveryStreamName = 'twitter-stream'

client = boto3.client('firehose', region_name='us-west-2',
                       aws_access_key_id=aws_key_id,
                       aws_secret_access_key=aws_key
                       )


# This is a basic listener that just prints received tweets and put them into the stream.


# class StdOutListener(StreamListener):

#     def on_data(self, data):

#         client.put_record(DeliveryStreamName=DeliveryStreamName, Record={
#                           'Data': json.loads(data)["text"]})
#         msg = json.loads(data)["text"]
#         print(msg)
#         return True

#     def on_error(self, status):
#         print(status)


def send_tweet(data):
    dictionary = {'text': data['text'],
                  'airline': data['airline']
    }
    
   
    client.put_record(DeliveryStreamName=DeliveryStreamName,
                      Record={'Data': data['text']})
    msg, air = data["text"], data["airline"]
    print(msg,"**", air)


def load_tweets(path_to_json):

    f = open(path_to_json)
    return json.load(f)


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    # l = StdOutListener()
    # auth = OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # stream = Stream(auth, l)
    # stream.filter(track=['realdonaldtrump'])

    index = 0
    stream_duration = 2
    tweets = load_tweets("tweets_sample.json")
    #for tweet in tweets:
        #print(type(tweet))
        #print(tweet)
    #    print(tweet["text"])
    #    time.sleep(random.randint(1, stream_duration))
    
    for tweet in tweets:
        # send a tweet
        send_tweet(tweet)
        # wait for some time
        time.sleep(random.randint(1, stream_duration))
        # if end of tweets break
