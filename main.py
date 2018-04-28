#!/usr/bin/python

from twython import *

app_token = open("consumer-key.apikey")
app_secret = open("consumer-secret.apikey")
auth_token = open("access-token.apikey")
auth_secret = open("access-token-secret.apikey")


twitter = Twython(
	app_key=app_token,
	app_secret=app_secret,
	oauth_otken=auth_token,
	oauth_otken_secret=auth_secret)

