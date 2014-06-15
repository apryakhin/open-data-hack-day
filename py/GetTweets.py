from twython import Twython


def getTweets(term, n=40):

	TWITTER_APP_KEY = 'ipJtC2iMpo2PnDGjr2srOTnP3'
	TWITTER_APP_KEY_SECRET = 'IOfZSaYi3GOafMXBN8XP2XwSrNKmnL3Xy9NHBB1X2lF7asYnDY' 
	TWITTER_ACCESS_TOKEN = '2427509917-Lf0EHFg7lTCxPXD1Mkkx4jP696r0KTjpAtEdCP0'
	TWITTER_ACCESS_TOKEN_SECRET = 'EmZQ6StuipbnlJwjCRgtFiDSS77PU21msLIY30y1YhtOG'

	t = Twython(app_key=TWITTER_APP_KEY, 
	            app_secret=TWITTER_APP_KEY_SECRET, 
	            oauth_token=TWITTER_ACCESS_TOKEN, 
	            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

	search = t.search(q=term,  
	                  count=n)

	tweets = search['statuses']


	summarizedTweets = {'name':term, 'tweets':[], 'links':[]}

	for tweet in tweets:
		for hashtag in tweet['entities']['hashtags']:
			summarizedTweets['links'].append(hashtag['text'])
		summarizedTweets['tweets'].append(tweet['text'])

	return [summarizedTweets]


 