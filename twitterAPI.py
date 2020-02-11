"""
Created on Thu Jan 30 13:02:52 2020
@author: Dakota Gravitt
"""

# twitter access
import tweepy
from twitter_keys import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

# get full text of tweet along with your API
def setupAPI():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

# returns public tweets as a list
def getPublicTweets(user, api, numOfPages):
    tweets = []
    for page in tweepy.Cursor(api.user_timeline, id=user, tweet_mode="extended").pages(numOfPages):
        tweets.extend(page)
    return tweets

# file I/O functions
import pickle

# will write a binary file of the tweets
def writeTweets(tweets_file, public_tweets):
    with open(tweets_file, 'wb') as f:
        pickle.dump(public_tweets, f)

# loads as list
def loadTweets(tweets_file):
    public_tweets = []
    with open(tweets_file, 'rb') as f:
       public_tweets = pickle.load(f)
    return public_tweets