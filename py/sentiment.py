import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sentiment
import GetTweets
import twitter
from collections import defaultdict

filenameAFINN = 'data/AFINN/AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(filenameAFINN) ]))

pattern_split = re.compile(r"\W+")


def sentiment(text):
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
    else:
        sentiment = 0
    return sentiment


def process(query):
    print 'start process'
    Tree = lambda: defaultdict(Tree)
    tree = Tree()
    for item in twitter.getTweets(query):
        hashtag = item['name']
        tweets = item['tweets']
        tree[hashtag]['links'] = {}
        for link in item['links']:
            link = link.decode("utf-8")
            tree[hashtag]['links'][link] = tree[hashtag]['link'].get(link, 0) + 1
        sentiments = [sentiment(item.encode("utf-8")) for item in tweets]
        tree[hashtag]['score'] = sum(sentiments)/math.sqrt(len(sentiments))
    return tree

if __name__ == '__main__':
    print process('munich')