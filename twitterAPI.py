# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:02:52 2020

@author: Dakota Gravitt - s523439
"""

# twitter access
import tweepy
from twitter_keys import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

def setupAPI():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

# file I/O functions
import pickle

def writeTweets(tweets_file, public_tweets):
    with open(tweets_file, 'wb') as f:
        pickle.dump(public_tweets, f)

def loadTweets(tweets_file):
    public_tweets = []
    with open(tweets_file, 'rb') as f:
        public_tweets = pickle.load(f)
    return public_tweets

# returns public tweets as a list
def getPublicTweets(user, api, numOfPages):
    public_tweets = []
    for status in tweepy.cursor(api.user_timeline, id=user).pages(numOfPages):
        tweets.extend(page)
    return public_tweets

