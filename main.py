#!/usr/bin/python

from twython import *
from getAllTweets import *

app_token = open("consumer-key.apikey")
app_secret = open("consumer-secret.apikey")
auth_token = open("access-token.apikey")
auth_secret = open("access-token-secret.apikey")


twitter = Twython(
	app_key=app_token,
	app_secret=app_secret,
	oauth_token=auth_token,
	oauth_token_secret=auth_secret)

getalltweets(twitter, "donaldtrump")
