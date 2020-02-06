# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:07:07 2020

@author: s523439
"""

#import tweepy
#import pickle
from twitterAPI import setupAPI, writeTweets, loadTweets, getPublicTweets

# always get API first
# grabs full text of tweets
api = setupAPI()

# define for your user and file names
user = 'jack'
files = 'jack.pkl'

# get tweets from a user
# grabbing only one page (or 20 full tweets)
public_tweets = getPublicTweets(user, api, 1)

# write tweets to file
writeTweets(files, public_tweets)

# load file
loadTweets(files)
#print(public_tweets)

tweet_texts = [status.text for status in public_tweets]
print(tweet_texts)