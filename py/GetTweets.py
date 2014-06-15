from twython import Twython
from collections import defaultdict
import json

def getTweets(term, n=1):

	TWITTER_APP_KEY = 'OMGTcMlp0HB1sY31MDdsvYaKn'
	TWITTER_APP_KEY_SECRET = 'Kk5WQPREcQA3AbMXVCs1hkMYqMCFldbUcyfTyKazIi7CckTQT1' 
	TWITTER_ACCESS_TOKEN = '2568849494-tHGymh8AM82zE6qmR8OLXQiA6lntfJzLbwirjt7'
	TWITTER_ACCESS_TOKEN_SECRET = '78N9uHCY5hbdlrEYMdbvktAidduhSaOW2azep98MwcqBM'

	t = Twython(app_key=TWITTER_APP_KEY, 
	            app_secret=TWITTER_APP_KEY_SECRET, 
	            oauth_token=TWITTER_ACCESS_TOKEN, 
	            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

	q= [term]
	
	seen = {}

	f = open('result.json', 'w')
	results = []
	i = 0
	try:
		while len(q) > 0:
			if i > 10:
				break
			i += 1
			print q
			term = q[0]
			q.pop(0)

			Tree = lambda: defaultdict(Tree)
			tree = Tree()

			search = t.search(q=term,  count=n)
			tweets = search['statuses']
			tree['name'] = term
			tree['tweets'] = []
			for tweet in tweets:
				tree['links'] = []
				for hashtag in tweet['entities']['hashtags']:
					if len(q) < 10 and hashtag['text'] not in seen:
						q.append(hashtag['text'])
						seen[hashtag['text']] = 1
					tree['links'].append(hashtag['text'])
				tree['tweets'].append(tweet['text'])
			results.append(tree)
	except Exception as e:
		print e
		f.write(json.dumps(results))
	f.write(json.dumps(results))


if __name__ == '__main__':
 	getTweets('brazil football')