import boto3
import random
import time
import json
import random

from configparser import ConfigParser

parser = ConfigParser()
parser.read('api_auth.cfg')

aws_key_id = parser.get('api_tracker', 'aws_key_id')
aws_key = parser.get('api_tracker', 'aws_key')

DeliveryStreamName = 'twitter-stream'

client = boto3.client('firehose', region_name='us-west-2',
                       aws_access_key_id=aws_key_id,
                       aws_secret_access_key=aws_key
                       )

def send_tweet(data):
   
    client.put_record(DeliveryStreamName=DeliveryStreamName,
                      Record={'Data': data['text'] + '|' + str(data['airline']) + '|' + str(data['tweet_created']) + '|' + str(data['tweet_location']) + '|' + str(data['user_timezone'])  })
    print(data['text'] + '|' + data['airline'] )


def load_tweets(path_to_json):

    f = open(path_to_json)
    return json.load(f)


if __name__ == '__main__':

    stream_duration = 1
    tweets = load_tweets("tweets.json")
    for tweet in tweets:
        # send a tweet
        send_tweet(tweet)
        # wait for some time
        time.sleep(random.randint(1, stream_duration))

