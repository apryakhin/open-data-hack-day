from twython import Twython


def getTweets(term, n=40):

	TWITTER_APP_KEY = 'OMGTcMlp0HB1sY31MDdsvYaKn'
	TWITTER_APP_KEY_SECRET = 'Kk5WQPREcQA3AbMXVCs1hkMYqMCFldbUcyfTyKazIi7CckTQT1' 
	TWITTER_ACCESS_TOKEN = '2568849494-tHGymh8AM82zE6qmR8OLXQiA6lntfJzLbwirjt7'
	TWITTER_ACCESS_TOKEN_SECRET = '78N9uHCY5hbdlrEYMdbvktAidduhSaOW2azep98MwcqBM'

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

	summarizedTweets['links'] = map(lambda x:x.lower(),summarizedTweets['links'])

	return [summarizedTweets]


 