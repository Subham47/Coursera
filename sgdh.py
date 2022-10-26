# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:28:59 2021

@author: subha
"""

from nltk.corpus import twitter_samples
from nltk.tag import pos_tag

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
print(pos_tag(tweet_tokens[0]))
print(tweet_tokens[0])
