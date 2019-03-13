
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

text = open("hp.txt").read()
phrases = tokenize.sent_tokenize(text)

sid = SentimentIntensityAnalyzer()

for sentence in phrases:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()