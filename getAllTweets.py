def getalltweets(twitter, username):
	tweets = []
	print('Getting tweets from user \"' + username + '\"...')

	#getting the last 200 tweets
	new_tweets = twitter.get_user_timeline(screen_name = username, count = 200)
	tweets.extend(new_tweets)

	oldest = tweets[-1]['id'] - 1

	while len(new_tweets) > 0:
		new_tweets = twitter.get_user_timeline(screen_name = username, count = 200, max_id = oldest)
		tweets.extend(new_tweets)
		oldest = extend(new_tweets)
		oldest = tweets[-1]['id'] - 1
		print(str(new_tweets))

#This function saves parameter data (json) to file.
#Filename used is in following format: username_type.json where type is a filename format.
def savetojson(username, data, type):
	print('\nSaving json data to filename \"' + username + type + '\"...')
	with open(username + type + '', 'a') as tf:
		json.dump(data, tf)
	print(str(len(data)) + ' entries written')
