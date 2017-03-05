import nltk
import pyexcel as pe
import pickle
from nltk.probability import FreqDist, ELEProbDist
from nltk.classify.util import apply_features, accuracy

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


pos_tweets = pe.get_array(file_name='pos.xlsx')

neg_tweets = pe.get_array(file_name='neg.xlsx')

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))



word_features = get_word_features(get_words_in_tweets(tweets))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def get_label(rev):
    f = open('classifier.pickle', 'rb')
    classifier = pickle.load(f)
    tweet = str(rev)
    x = classifier.classify(extract_features(tweet.split()))
    f.close()
    return x