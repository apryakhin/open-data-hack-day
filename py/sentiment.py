import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sentiment
import GetTweets
import twitter
import json
from collections import defaultdict
from operator import itemgetter

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
    id = 0
    results = {}
    for item in twitter.getTweets(query):
        tree = Tree()
        hashtag = item['name']
        tweets = item['tweets']
        tree['name'] = hashtag
        tree['id'] = id
        tmp = {}
        for link in item['links']:
            link = link.decode("utf-8")
            tmp[link] = tmp.get(link, 0) + 1
        tree['links'] = sorted(tmp.iteritems(), key=itemgetter(1), reverse=True)
        sentiments = [sentiment(item.encode("utf-8")) for item in tweets]
        tree['score'] = sum(sentiments)/math.sqrt(len(sentiments))
        results[hashtag] = tree
        id += 1
    #convert the graph
    sorted_results = sorted(results, key=itemgetter('score'), reverse=True)
    graph = Tree()
    graph['nodes'], graph['links'] = [], []
    for hashtag in results.iteritems():
        graph['nodes'].append({'name': sorted_results[i]['name'], 'score': sorted_results[i]['score']})
        j = i
        for link, score in sorted_results[i]['links']:
            graph['links'].append( {'source': j, 'target': i, 'count': score})
            j += 1

    f = open('../data/graph.json', 'w')
    f.write(json.dumps(graph))
    return graph

if __name__ == '__main__':
    print process('munich')