# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:07:07 2020

@author: s523439
"""

#import tweepy
#import pickle
from twitterAPI import setupAPI, writeTweets, loadTweets, getPublicTweets

# always get API first
api = setupAPI()

# define for your user and file names
user = 'jack'
file = '___.pkl'

# get tweets from a user
public_tweets = getPublicTweets(user, api)

# write tweets to file
writeTweets(file, public_tweets)

# load file
loadTweets(file)
#print(public_tweets)

tweet_texts = [status.text for status in public_tweets]
print(tweet_texts)