"""
Created on Thu Jan 30 13:02:52 2020
@author: Dakota Gravitt
"""

# twitter access
import tweepy
from twitter_keys import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

# access API with your keys
def setupAPI():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True) # should simply wait on rate limit to replenish. May take longer to perform below actions.

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

# load text of tweets after writing to file
def grabTextTweets(api, user, fileName, numOfPages):
    # grab tweets based on above parameters
    public_tweets = getPublicTweets(user, api, numOfPages)
    # write tweets to a file
    writeTweets(fileName, public_tweets)
    # load the text of each tweet only
    tweet_texts = [status.full_text for status in public_tweets]
    return tweet_texts

# only keep tweets that are not retweets
def loadNoRetweets(tweets_file):
    public_tweets = loadTweets(tweets_file)
    # make list of true and false for each tweet
    retweeted = [status.retweeted for status in public_tweets]
    #print(retweeted) # print in case you would like to see which tweets are retweets
    for i in range(len(public_tweets)-1):
        if retweeted == True:
            public_tweets.remove(public_tweets[i])
    return public_tweets

import time
import datetime
# get many users' tweets at once from a list of users
def mass_status_grab(users_list, api, numOfPages):
    start_all = time.time()
    statuses = []
    for user in users_list:
        # will time each grab
        start = 0
        end = 0
        start = time.time()

        # get tweets, store them in a binary file named after the user
        statuses = getPublicTweets(user, api, numOfPages)
        user = str(user) # convert user var into a string in case an integer id was passed instead of a screen name
        file_name = user + '.pkl'
        writeTweets(file_name, statuses) # pickle statuses before everything breaks and we must commit seppuku

        # print how long 
        end = time.time()
        seconds = end - start
        print(user, ' saved in', seconds, 'seconds w/', len(statuses), 'tweets')
    
    # show overall time to save each user's tweets
    end_all = time.time()
    seconds_all = end_all - start_all
    print("\nSaved all users' tweets in ", seconds_all, 'seconds')