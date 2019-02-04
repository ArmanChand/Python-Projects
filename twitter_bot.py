import tweepy
import argparse

parser = argparse.ArgumentParser(description='Provide your tweet')
parser.add_argument('-t', action="store", dest="t")
parser.add_argument('-rt', action="store", dest = "rt")
parser.add_argument('--tl', action="store_true", default=False)
args = parser.parse_args()

consumer_key = 'yCwyUQfQckYuiu6t8ArZIDOSh '
consumer_secret = 'EjYXFYN7MRXUeQ4LBLeKenPhpncZY0guNNh6QhCfvSgQLW2ZJB'

access_token = '1366496006-vtMDTnM2XVDrfSKfndySVtgcu8Y1lEAyPZotRUB'
access_token_secret = 'CL5OmPMoGCqLHzSx9e1MG1nVzhnGKy6za3kffv5YG8w76'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
if args.tl:
    for tweet in api.home_timeline():
        print(tweet.text)
        print(tweet.id)
        print("\n")
if args.t:
    api.update_status(args.t)
    print("Your tweet successfully posted!!")
if args.rt:
    api.retweet(args.rt)
    print("Your retweet successfully done!")

