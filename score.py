import gensim.models as g
import codecs
from gensim import utils
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
import os
import numpy as np

model = "./imdb.d2v"


def read_words(s):
    word = s.split()
    return word


def get_score(s):
    words1 = read_words(s)
    l = len(words1)
    m = g.Doc2Vec.load(model)
    sumf = 0

    for word in words1:
        try:
            vec = m[word]
            if np.sum(vec) < 0:
                l += 3

            sumf += np.sum(vec)
        except KeyError:
            sumf += 0
            l -= 1
    if l < 15:
        score = sumf / 15
    else:
        score = sumf / l
    return score
